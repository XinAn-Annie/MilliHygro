import cv2, numpy as np, os, math
from PIL import Image
src=r'C:\Users\Lenovo\Desktop\C8185670-8AE3-49FD-AA96-444F761DC818-486-000000694BA4F641.png'
out=r'D:\codex\butterfly_layered.svg'
im=cv2.imread(src, cv2.IMREAD_UNCHANGED)
if im.shape[2]==4:
    b,g,r,a=cv2.split(im)
else:
    b,g,r=cv2.split(im); a=np.full(b.shape,255,np.uint8)
rgb=cv2.merge([r,g,b])
# foreground: saturated colored pixels; crop to art bounds
sat=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV)[:,:,1]
val=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV)[:,:,2]
fg=((a>10)&(sat>25)&(val<250)).astype(np.uint8)
ys,xs=np.where(fg>0)
x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max()
pad=8; x0=max(0,x0-pad); y0=max(0,y0-pad); x1=min(rgb.shape[1]-1,x1+pad); y1=min(rgb.shape[0]-1,y1+pad)
roi=rgb[y0:y1+1,x0:x1+1]; roia=a[y0:y1+1,x0:x1+1]
# sample colored pixels for kmeans
mask=((roia>10)&(cv2.cvtColor(roi,cv2.COLOR_RGB2HSV)[:,:,1]>25)&(cv2.cvtColor(roi,cv2.COLOR_RGB2HSV)[:,:,2]<250))
data=roi[mask].reshape(-1,3).astype(np.float32)
K=6
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,80,0.25)
_, labels, centers=cv2.kmeans(data,K,None,criteria,8,cv2.KMEANS_PP_CENTERS)
centers=np.uint8(np.clip(centers,0,255))
# sort by approximate hue then luminance for stable layer order
hsvc=cv2.cvtColor(centers.reshape(1,K,3),cv2.COLOR_RGB2HSV).reshape(K,3)
order=sorted(range(K), key=lambda i:(int(hsvc[i,0]), -int(hsvc[i,1])))
# assign nearest center to all pixels, colored only
flat=roi.reshape(-1,3).astype(np.float32)
d=((flat[:,None,:]-centers[None,:,:].astype(np.float32))**2).sum(2)
idx=np.argmin(d,axis=1).reshape(roi.shape[:2])
# Catmull-Rom closed path -> cubic

def path_from_contour(cnt):
    pts=cnt[:,0,:].astype(float)
    peri=cv2.arcLength(cnt,True)
    eps=max(2.2,0.009*peri)
    ap=cv2.approxPolyDP(cnt,eps,True)[:,0,:].astype(float)
    if len(ap)<4: return ''
    # remove near duplicates
    p=[]
    for q in ap:
      if not p or np.linalg.norm(q-p[-1])>1.5: p.append(q)
    if len(p)>2 and np.linalg.norm(p[0]-p[-1])<1.5:p.pop()
    n=len(p)
    if n<3:return ''
    s=f'M {p[0][0]:.1f},{p[0][1]:.1f}'
    for i in range(n):
      p0=np.array(p[(i-1)%n]); p1=np.array(p[i]); p2=np.array(p[(i+1)%n]); p3=np.array(p[(i+2)%n])
      c1=p1+(p2-p0)/6.0; c2=p2-(p3-p1)/6.0
      s+=f' C {c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}'
    return s+' Z'

names=[]
for oi,k in enumerate(order):
    # mask only colored pixels assigned cluster
    m=((idx==k)&mask).astype(np.uint8)*255
    # clean isolated noise, close tiny gaps
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
    m=cv2.GaussianBlur(m,(7,7),0); _,m=cv2.threshold(m,128,255,cv2.THRESH_BINARY); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))
    n,lab,stats,cent=cv2.connectedComponentsWithStats(m,8)
    clean=np.zeros_like(m)
    for j in range(1,n):
      if stats[j,cv2.CC_STAT_AREA]>=80: clean[lab==j]=255
    m=clean
    contours,hier=cv2.findContours(m,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    if hier is None: continue
    paths=[]
    for j,c in enumerate(contours):
      area=cv2.contourArea(c)
      if area<80: continue
      # only outer contours; holes are included by evenodd with their own paths
      paths.append(path_from_contour(c))
    if not paths: continue
    color=centers[k].tolist(); col='#%02x%02x%02x'%tuple(color)
    names.append((oi,col,len(paths)))
    # y-up not needed, SVG y-down matches image
    print(f'layer {oi} {col} {len(paths)}')
    if oi==0: svg=[]
# Build SVG
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x1-x0+1} {y1-y0+1}" width="1200" role="img" aria-label="Simplified layered butterfly">', '<title>Layered butterfly</title>', '<desc>Color separated smooth vector layers. Each layer uses even-odd paths so inner colors are cut out.</desc>']
for oi,k in enumerate(order):
    m=((idx==k)&mask).astype(np.uint8)*255
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
    m=cv2.GaussianBlur(m,(7,7),0); _,m=cv2.threshold(m,128,255,cv2.THRESH_BINARY); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))
    n,lab,stats,cent=cv2.connectedComponentsWithStats(m,8); clean=np.zeros_like(m)
    for j in range(1,n):
      if stats[j,cv2.CC_STAT_AREA]>=80: clean[lab==j]=255
    contours,hier=cv2.findContours(clean,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    paths=[path_from_contour(c) for c in contours if cv2.contourArea(c)>=80]
    paths=[p for p in paths if p]
    if not paths: continue
    col='#%02x%02x%02x'%tuple(centers[k].tolist())
    svg.append(f'  <g id="layer-{oi+1}" data-color="{col}" fill="{col}" fill-rule="evenodd">')
    for p in paths: svg.append('    <path d="'+p+'"/>')
    svg.append('  </g>')
svg.append('</svg>')
open(out,'w',encoding='utf-8').write('\n'.join(svg))
print('written',out,'size',os.path.getsize(out),'viewbox',x1-x0+1,y1-y0+1)

