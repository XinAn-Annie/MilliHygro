/* Bitmap layer helpers. Original artwork is kept separately from its material driver. */
window.PngLayers = (() => {
  const isPng = value => /^data:image\/png;base64,[a-z0-9+/=\s]+$/i.test(value || '');
  const basename = value => { try { return decodeURIComponent(value).replace(/\\/g, '/').split('/').pop(); } catch { return value; } };
  async function resolveImages(root, files) {
    const missing = new Set();
    for (const node of root.querySelectorAll('image')) {
      const href = node.getAttribute('href') || node.getAttributeNS('http://www.w3.org/1999/xlink', 'href') || '';
      if (isPng(href)) continue;
      const name = basename(href), file = files.get(name) || (files.size===1 ? files.values().next().value : null);
      if (!file) { missing.add(name || '(unnamed PNG)'); continue; }
      const bytes = new Uint8Array(await file.slice(0, 8).arrayBuffer());
      if (bytes.join(',') !== '137,80,78,71,13,10,26,10') throw Error('Invalid PNG: ' + name);
      const data = await new Promise((resolve, reject) => { const reader = new FileReader(); reader.onload = () => resolve(reader.result); reader.onerror = reject; reader.readAsDataURL(file); });
      node.removeAttributeNS('http://www.w3.org/1999/xlink', 'href');
      node.setAttribute('href', String(data).replace(/^data:[^;]+;/, 'data:image/png;'));
    }
    if (missing.size) throw Error('Select linked PNG files: ' + [...missing].join(', '));
  }
  function whiteAlpha(canvas) {
    const out = document.createElement('canvas'); out.width = canvas.width; out.height = canvas.height;
    const ctx = out.getContext('2d'); ctx.drawImage(canvas, 0, 0); ctx.globalCompositeOperation = 'source-in'; ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, out.width, out.height);
    return out;
  }
  function lab(r, g, b) {
    const linear = v => { v /= 255; return v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; };
    r = linear(r); g = linear(g); b = linear(b);
    const f = v => v > .008856 ? Math.cbrt(v) : 7.787 * v + 16 / 116;
    const x = f((.4124564*r + .3575761*g + .1804375*b)/.95047), y = f(.2126729*r + .7151522*g + .072175*b), z = f((.0193339*r + .119192*g + .9503041*b)/1.08883);
    return [116*y-16, 500*(x-y), 200*(y-z)];
  }
  // Deterministic alpha-weighted histogram, then nearby perceptual-color groups.
  // White is a valid color; only transparent pixels are excluded. DeltaE radius: 12.
  function dominant(canvas) {
    const sample = document.createElement('canvas'), scale = Math.min(1, 320 / Math.max(canvas.width, canvas.height));
    sample.width = Math.max(1, Math.round(canvas.width*scale)); sample.height = Math.max(1, Math.round(canvas.height*scale));
    const ctx = sample.getContext('2d', {willReadFrequently:true}); ctx.drawImage(canvas, 0, 0, sample.width, sample.height);
    const data = ctx.getImageData(0,0,sample.width,sample.height).data, bins = new Map(); let total = 0;
    for (let i=0;i<data.length;i+=4) {
      const w=data[i+3]/255; if (!w) continue;
      const key=(data[i]>>3)*1024+(data[i+1]>>3)*32+(data[i+2]>>3);
      let bin=bins.get(key); if (!bin) { bin={key,w:0,r:0,g:0,b:0}; bins.set(key,bin); }
      bin.w+=w; bin.r+=data[i]*w; bin.g+=data[i+1]*w; bin.b+=data[i+2]*w; total+=w;
    }
    if (!total) throw Error('PNG layer has no visible pixels');
    const groups=[];
    for (const bin of [...bins.values()].sort((a,b)=>b.w-a.w||a.key-b.key)) {
      const color=lab(bin.r/bin.w,bin.g/bin.w,bin.b/bin.w); let best=null, distance=144;
      for (const group of groups) { const d=color.reduce((sum,v,i)=>sum+(v-group.lab[i])**2,0); if(d<distance){distance=d;best=group;} }
      if (!best) { best={w:0,r:0,g:0,b:0,lab:color}; groups.push(best); }
      best.w+=bin.w; best.r+=bin.r; best.g+=bin.g; best.b+=bin.b;
    }
    const winner=groups.sort((a,b)=>b.w-a.w)[0];
    const hex='#'+[winner.r,winner.g,winner.b].map(v=>Math.round(v/winner.w).toString(16).padStart(2,'0')).join('').toUpperCase();
    return {hex,share:winner.w/total,groups:groups.length};
  }
  return {isPng,resolveImages,whiteAlpha,dominant};
})();
