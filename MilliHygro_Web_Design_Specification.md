# MilliHygro Web Interface — 完整视觉与交互设计规范

> 版本：1.0  
> 日期：2026-08-14  
> 适用对象：MilliHygro 当前 HTML 原型及其后续同系列网页界面  
> 原则：本规范首先记录**当前已经实现的视觉系统**，再把它整理成可持续执行的设计规则。除非后续明确改版，否则新增组件应优先复用这里的 token、尺寸、间距与交互状态。

---

## 1. 设计目标

MilliHygro 是研究型材料设计工具，不是营销页。界面视觉应服务于四件事：

1. **让设计对象成为视觉中心**：3D 形变和 Front/Back Print 的面积必须明显大于控制区。
2. **让制造参数可追溯**：颜色、CMYK、曲率、纤维方向、尺寸与导出动作应具有稳定层级。
3. **让非专业用户能顺序操作**：右栏严格维持 01→04 的任务流程。
4. **让论文截图稳定一致**：字号、间距、边框、选中态、控制密度尽量使用固定 token，减少“每个组件自己长一套”的问题。

视觉关键词：

```text
Technical / Calm / Precise / Research-oriented / Lightweight / Manufacturing-aware
```

不采用：

```text
高饱和大面积品牌色、强阴影卡片、圆润消费级 App 风格、装饰性渐变背景、复杂玻璃拟态
```

---

## 2. 设计 Token：唯一视觉源

### 2.1 字体

```css
--font-ui: "Open Sans", Arial, sans-serif;
```

优先级：

1. Open Sans；
2. Arial；
3. 系统 sans-serif。

Google Fonts 当前加载：

```text
Open Sans 400 / 600 / 700 / 800
Open Sans italic 400
```

**规范要求**：

- 网页 UI 不再混用 Georgia、Times、PingFang 等独立视觉字体；
- 英文 UI、数字、单位、按钮统一 Open Sans；
- 中文若未来加入，仍使用同一 font-family stack，让系统 fallback 处理中文字形；
- 不为单个组件另起字体。

---

## 3. 字号体系

当前系统以约 10.5–22.5 px 的紧凑研究工具字号为主。

### 3.1 推荐语义字号

| Token | 建议值 | 当前对应场景 | 字重 |
|---|---:|---|---:|
| `type-xxs` | 10.5 px | 卡片副信息、CMYK 辅助信息、尺寸限制 | 400–700 |
| `type-xs` | 12 px | 小标签、Section 描述、按钮辅助说明 | 400–800 |
| `type-sm` | 13.5 px | Select、字段标签、主要表单值 | 600–700 |
| `type-md` | 15 px | 3D Size Status、局部强调值 | 600 |
| `type-lg` | 16.5 px | 曲率大值、旧兼容组件主要值 | 600–700 |
| `type-xl` | 18 px | 3D RH/Fiber/Curvature 状态 | 700 |
| `type-section` | 19.5 px | 01–04 Section 标题 | 700 |
| `type-brand` | 22.5 px | MilliHygro 品牌名 | 700 |

### 3.2 行高

- Section 标题：`1.3`；
- 卡片主标题：约 `1.25`；
- 小型辅助说明：`1.35–1.45`；
- 不建议正文型 UI 使用小于 `1.25` 的 line-height。

### 3.3 字重

| 用途 | Weight |
|---|---:|
| 普通辅助信息 | 400 |
| 普通按钮/状态 | 600 |
| 字段标签/主要数值 | 700 |
| 编号/极小强调 | 800 |

### 3.4 大小写

- `Front Print`、`Back Print`：Title Case；
- `Front Part Colors`、`Back Part Colors`：Title Case；
- 状态值：`RH = 100%`、`Fiber = 90°`；
- 不要大面积全大写；仅极小的技术标签可以使用 uppercase。

---

## 4. 间距系统

当前网页已经明确采用：

```text
4 px base unit
```

### 4.1 Token

```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 24px;
--space-6: 32px;
--space-7: 40px;
--space-8: 48px;
```

### 4.2 使用原则

- **4 px**：同一控件内部极小文字/数值关系；
- **8 px**：小控件内部、色块与文字、输入框并列；
- **12 px**：同组控件常规间隔；
- **16 px**：Section 内主要 padding、模块内部明显层级；
- **24 px**：大视图区内边距、画布与 readout 的大间隔；
- **32 / 40 / 48 px**：只用于页面级或视觉留白，不用于右栏紧凑表单的常规间距。

### 4.3 垂直节奏

右侧控制栏：

```text
scroll padding       = 12 px
section gap          = 12 px
section padding      = 16 px
section title bottom = 16 px
field label bottom   = 8 px
mode tabs top        = 12 px
color editor top     = 12 px
range top            = 16 px
export item gap      = 12 px
```

**禁止**在同一层级随意使用 5、7、9、13、18、22 px 作为新间距；如果确有视觉原因，必须说明它是光学修正而不是新 token。

---

## 5. 主配色

### 5.1 核心语义变量

| Token | HEX | 用途 |
|---|---|---|
| `--ink` | `#202226` | 主文字、深色强调 |
| `--muted` | `#747980` | 次级信息 |
| `--line` | `#C9CED8` | 主分隔线 |
| `--paper` | `#FFFFFF` | 页面背景 |
| `--panel` | `#F7F8FA` | 面板浅底 |
| `--accent` | `#6379B7` | 选中、focus、交互强调 |
| `--accent-soft` | `#DFE5F4` | Section 标题底色 |
| `--control-surface` | `#FAFBFC` | 表单/导出浅底 |
| `--selected-surface` | `#F8FAFF` | 选中卡片浅底 |

### 5.2 当前辅助中性色

```text
#343942  深色按钮/编号
#545A63  字段信息
#646970  品牌副信息
#70757C  视图标签
#717782  小技术标签
#7F858E  辅助读数
#8A8F98  弱提示
#AEB6C4  主面板边线
#BFC6D3  工作区分隔
#C2C8D2  Section 边框
#D1D5DC  小卡片边框
#E2E3E5  品牌栏底色
#F3F4F6  右侧面板底色
```

### 5.3 配色原则

- Accent 只承担“可交互/已选中/focus”语义；
- 不把 Accent 用作大面积背景；
- 制造数据颜色（用户所选材料色）与 UI Accent 必须区分；
- Cut/Crease 的工程语义色不应被 UI 品牌色替代。

### 5.4 工程语义色

当前代码：

- Cutting preview：`#EE365D`；
- Crease guide：`#2F80ED`；
- Crease print fill：`#FFFFFF`；
- Outline / motif dark line：约 `#20232A / #25282D`。

如果后续修改：

- Cut 必须始终与 Crease 可视觉区分；
- 白色 crease 区的“CMYK=0”制造语义优先于装饰需求；
- 论文图例中应复用同样语义。

---

## 6. 页面栅格

### 6.1 Desktop > 1100 px

```text
.layout
├─ workspace: 72fr
└─ controls : 28fr, min 380 px
```

### 6.2 Workspace 垂直分区

常规：

```text
3D panel     = 62fr
pattern view = 38fr
```

较窄桌面（≤900 px）现有兼容规则：

```text
3D panel     = 58fr
pattern view = 42fr
```

### 6.3 ≤1100 px

```text
workspace = fluid
controls  = 360 px
```

### 6.4 ≤820 px

- 主布局改 block；
- workspace 高度约 900 px；
- 3D 区约 540 px；
- pattern views 区约 360 px；
- 右栏移到下方；
- 页面允许纵向滚动。

---

## 7. 3D 视图区规范

### 7.1 背景

- 纯白 `#FFFFFF`；
- 不增加装饰背景、网格纸纹理或渐变，除非它直接帮助空间判断。

### 7.2 Scene Meta

位置：

```text
top   = 16 px
left  = 24 px
right = 24 px
```

主要状态：18 px / 700。

Size Status：15 px / 600，右对齐。

显示顺序：

```text
RH
Fiber
Curvature                         SelectedOutline · size
```

### 7.3 Gesture Hint

```text
Drag to rotate · Scroll to zoom
```

- left 24 px；
- bottom 16 px；
- padding 8 × 12 px；
- 白色半透明底；
- 1 px 浅灰边框；
- 不使用强阴影。

---

## 8. Front / Back Print 视图区规范

每个 `.pattern-view`：

```text
2-column grid
left  = minmax(150px, 1fr)
right = minmax(170px, 220px)
gap   = 24px
padding = 24px 24px 44px
```

### 8.1 Canvas

```text
width <= 260px
width <= 100% of left column
square aspect ratio
centered in left column
```

### 8.2 Part Colors Readout

- 必须位于 Canvas 右侧；
- `max-width: 220px`；
- `padding: 12px`；
- 不使用 absolute 覆盖 Canvas；
- 不使用重阴影；
- Part row：色块 32×32 px，文字区自适应。

### 8.3 View Label

`Front Print` / `Back Print`：

- 左下定位；
- 16.5 px；
- weight 600；
- `#70757C`。

---

## 9. 右侧控制栏规范

### 9.1 容器

```text
background = #F3F4F6
left border = 1px #AEB6C4
```

### 9.2 Brand Bar

```text
height  = 64 px
padding = 0 16 px
bg      = #E2E3E5
```

MilliHygro：22.5 px。

### 9.3 Scroll Area

```text
padding = 12 px
height  = viewport - 64 px
```

Scrollbar 应保持低对比度，不成为视觉焦点。

---

## 10. Section 规范

每个 `01 / 02 / 03 / 04`：

```text
margin-bottom = 12 px
padding       = 16 px
border        = 1 px #C2C8D2
background    = #FFFFFF
corner        = 0 / very small (current square technical style)
```

### 10.1 Section Header

通过负 margin 拉到 Section 边缘：

```text
padding = 12px 16px
background = #DFE5F4
border-bottom = 1px #C3C9D4
```

### 10.2 编号块

```text
28 × 28 px
background = #343942
text = white
font-size = 12 px
font-weight = 800
border-radius = 1 px
```

### 10.3 标题

```text
19.5 px
line-height 1.3
```

### 10.4 描述

当前多数 `<p>` 留空；如果未来添加：

```text
12 px
#747B86
margin-top 2 px
```

描述应解释任务，不重复标题。

---

## 11. Outline / Pattern 选择卡片

### 11.1 栅格

```text
3 columns
gap = 12 px
```

### 11.2 卡片

```text
min-height = 112 px
padding = 12px 8px 14px
gap = 10 px
border = 1px #D1D8E8
background = white
radius = 4 px
```

### 11.3 Hover

- 边框 → `#8496C5`；
- 不位移；
- 不使用浮起阴影。

### 11.4 Selected

```text
border = #7187C2
background = #F8FAFF
box-shadow = inset 0 -7px 0 #DFE6FB + 1px outline
```

**所有 Outline 与 Pattern 的选中态必须一致。**

### 11.5 Thumbnail

Outline：约 56×44 px。  
Pattern：约 56×44 px，并有 1 px 外框。

缩略图是“识别图标”，不是工程输出，不应承担尺寸精度。

---

## 12. Proportional Size 控件

容器：

```text
margin-top = 12 px
padding    = 12 px
border     = 1 px #C8CED9
background = #FAFBFC
```

顶部：标签 + 当前尺寸。

底部：

```text
Min size | Scale × | Max size
```

信息层级：

- 当前尺寸：13.5 px；
- 上下限：10.5 px；
- 主要标签：12 px / 700。

---

## 13. Tabs / Mode Switch

适用于：

```text
Solid Color
Color Gradient
Concentration Gradient
```

### 13.1 容器

```text
background = #ECEEF2
radius = 2 px
```

### 13.2 单个按钮

```text
min-height = 44 px
padding = 8px 6px
font-size ≈ 12 px
```

### 13.3 Active

```text
background = white
bottom inset line = 2 px #6379B7
text = #202226
```

不使用“整块紫底白字”的重品牌样式。

---

## 14. Select / Form Field

### 14.1 Field Label

```text
font-size = 13.5 px
font-weight = 700
color = #545A63 / #777A80 family
margin-bottom = 8 px
```

### 14.2 Select

```text
height = 44 px
padding-x = 12 px
border = 1 px #C8CDD6
background = white
font-size = 13.5 px
radius ≈ 1 px
```

### 14.3 Focus

所有 button / input / select：

```text
outline = 2px solid #6379B7
offset  = 2px
```

不得为了“更干净”删除 keyboard focus indicator。

---

## 15. Color Picker 规范

### 15.1 容器

```text
padding = 16 px
border = 1 px #AEB7C7
background = white
```

### 15.2 当前色

右上/顶部展示：

- 小色块 18×18 px；
- HEX 12 px；
- 仅显示当前值，不增加旧版“预设颜色圆点”组件。

### 15.3 SV Plane

当前：

```text
height = 142 px
border = 1 px #AEB5C0
cursor = crosshair
```

### 15.4 Hue Strip

```text
height = 15 px
margin-top = 12 px
```

### 15.5 CMYK Inputs

四列等宽：

```text
C | M | Y | K
```

- grid gap 8 px；
- 单元 padding 8 px；
- input height 32 px；
- 数字右对齐；
- 单通道 0–100。

**不要重新加入 HEX 底部冗余大标签。** HEX 只在当前色头部简洁显示。

---

## 16. Gradient Preset 规范

当前 2 列：

```text
grid-template-columns = repeat(2, 1fr)
gap = 12 px
```

单卡：

```text
padding = 12 px
border = 1 px #CDD1D8
background = #FAFBFC
```

Swatch：

```text
height = 32 px
margin-bottom = 8 px
```

Selected：Accent 边框 + very light accent surface。

---

## 17. Range Slider 规范

### 17.1 垂直结构

```text
Label ---------------- Value
[===========●==========]
```

### 17.2 间距

- group top：16 px；
- label → slider：8 px。

### 17.3 轨道

```text
height = 4 px
background = #DEDDD8
accent = #6379B7
```

### 17.4 Thumb

```text
15 × 15 px
white center
4 px accent border
```

### 17.5 数值格式

- 角度：整数 + `°`；
- 比例：两位小数 + `×`；
- 曲率：三位小数 + `× 10⁻³ rad/m`；
- 尺寸：最多 2 位小数 + `mm`。

---

## 18. Maximum / Actual Curvature 信息层级

`Maximum Deformable Curvature` 是计算结果，不是普通输入。

容器：

```text
margin-top = 16 px
padding = 16 px
border = 1 px #AFBAD4
background = #F6F8FD
```

Label：13.5 px / 700。  
Value：16.5 px，偏蓝技术色 `#354F91`。

`Actual Deformation Curvature` 是用户输入，继续使用 Range 组件。

两者必须保持：

```text
Maximum = material capability / upper bound
Actual  = chosen signed deformation value
```

不要把二者名称互换。

---

## 19. Export 组件规范

2 列布局：

```text
Print pattern | Cutting Path
```

单按钮：

```text
min-height = 68 px
padding = 12 px
border = 1 px #CCD1D9
background = #FAFBFC
gap = 12 px
```

Hover：边框变 Accent；不改变背景为高饱和色。

图标：约 22.5 px，Accent 色。

主标题：13.5 px。  
副标题：12 px 以下的辅助信息。

制造文件名称必须明确文件格式和关键语义：

```text
Front + mirrored back · A4 PDF
CAD DXF · mm units
```

---

## 20. 边框与圆角

### 20.1 当前风格

MilliHygro 现行版采用**低圆角、工程面板化**视觉：

- Section：近直角；
- 输入框：1–2 px；
- 卡片：4 px；
- 颜色读数卡：直角/低圆角；
- 不使用 12–20 px 的大圆角卡片体系。

### 20.2 边框层级

```text
主结构边界  #AEB6C4 / #BFC6D3
Section      #C2C8D2
Control      #C8CDD6 / #CDD1D8
弱分隔       #E1E4EA
```

边框比阴影优先。

---

## 21. 阴影

现行原则：**极少使用阴影**。

允许：

- 小型临时 Toast；
- 交互 handle 的极轻阴影；
- 旧 color picker handle。

不允许：

- Section 大面积浮层阴影；
- 每张卡片默认 drop shadow；
- 3D 视图区用装饰阴影制造“卡片感”。

研究工具优先使用边界、对齐和留白建立层级。

---

## 22. 图标规范

当前大量使用文本符号/简单 SVG：

- Export：`↓`、`✂`；
- Pattern/Outline：内嵌 SVG；
- Color handle：纯 CSS。

后续新增图标：

- 优先使用同一套线性 SVG；
- 默认 stroke 1–1.5 px；
- 颜色使用 Ink / Muted / Accent；
- 不混用 3D emoji、彩色系统 icon 与工程线性 icon。

---

## 23. 文案规范

### 23.1 动作型标题

继续使用：

```text
Select Outline
Select Pattern
Region & Color
Export Manufacturing Files
```

### 23.2 制造术语统一

推荐固定：

```text
Front Print
Back Print
Front Part Colors
Back Part Colors
Maximum Deformable Curvature
Actual Deformation Curvature
Fiber Direction
Gradient Direction
Cutting Path
```

不要在不同位置交替使用：

```text
Front View / Front Pattern / Front Printing / Front Side Image
```

除非语义确实不同。

### 23.3 单位格式

统一空格：

```text
10 mm
12 × 5 mm
90°
100%
0.750 × 10⁻³ rad/m
```

---

## 24. 状态规范

### 24.1 Default

白底 + 中性边框。

### 24.2 Hover

边框轻微向 Accent 靠近；不平移、不放大。

### 24.3 Selected

Accent border + pale accent surface + bottom inset emphasis。

### 24.4 Focus-visible

2 px Accent outline + 2 px offset。

### 24.5 Disabled

当前系统暂无统一 disabled 组件。如果未来增加：

- opacity 约 0.45–0.55；
- cursor not-allowed；
- 不只依赖颜色变化，还应确保按钮不可触发。

### 24.6 Error

当前无统一 Error token。未来建议只为真实输入错误建立：

```text
border / text = muted red
background = very pale red
```

不要复用工程 Cut 红色作为表单 Error 色，避免语义冲突。

---

## 25. 响应式规范

### Desktop First

MilliHygro 主要面向桌面设计工作，因此 3D + 双面打印 + 控制栏是首要场景。

### ≤1100 px

- 控制栏缩到 360 px；
- Print Preview 的 readout 变窄；
- pattern view gap 由 24 px 降到 12 px；
- 颜色色块由 32 px 降到 24 px。

### ≤820 px

- 左右两栏堆叠；
- 页面恢复纵向滚动；
- 不应隐藏核心功能；
- 控制栏边界从 left border 转为 top border。

### 进一步移动端

当前不是移动优先工具。若未来必须支持手机，建议另做响应式信息架构，不要单纯继续缩小所有字号。

---

## 26. 可访问性规范

当前已经具备：

- `focus-visible`；
- 部分 `aria-label`；
- Color readout `aria-live="polite"`；
- button / select / input 使用原生元素。

后续必须继续：

1. 所有纯图标按钮增加 `aria-label`；
2. 颜色选择不能只靠颜色区分 selected 状态；
3. 不删除 keyboard focus；
4. 小字号文字需保持足够清晰，不继续压缩到 9 px 级别；
5. 工程语义 Cut/Crease 最好同时依赖线型/虚实，而不是只靠红/蓝。

---

## 27. 数据可视化与材料颜色规范

页面中存在两套“颜色”：

### A. UI Color

例如 Accent `#6379B7`，用于交互状态。

### B. Material / Print Color

用户在 `Region & Color` 中选择的颜色，用于：

- 2D preview；
- 3D texture；
- CMYK/material mapping；
- Front/Back manufacturing readout。

**两套颜色不可混为一谈。**

材料颜色绝不能因为界面换主题就改变。

---

## 28. 论文截图规范

用于 CHI 论文展示时建议统一：

- 浏览器宽度：1440 px 或稳定桌面宽度；
- 页面缩放：100%；
- 使用同一外轮廓尺寸；
- 截图前确认 RH / Fiber / Curvature 状态可见；
- 右栏滚动到需要展示的 Section；
- Front/Back Part Colors 不遮挡画布；
- 不在截图时打开浏览器 DevTools；
- 同组对比图保持相同 Camera、Fiber、RH，只改变被研究变量。

如果比较“颜色导致的材料响应差异”，应单独记录：

```text
HEX
CMYK
CMYK Sum
Maximum Curvature
Actual Curvature
RH
Fiber Direction
Outline / Pattern / Scale
```

---

## 29. CSS 新增规则的书写规范

### 29.1 优先 Token

正确：

```css
.my-control {
  gap: var(--space-3);
  padding: var(--space-4);
  color: var(--ink);
  border: 1px solid var(--line);
}
```

不推荐：

```css
.my-control {
  gap: 13px;
  padding: 19px;
  color: #1f2024;
  border: 1px solid #c7ccd5;
}
```

### 29.2 选择器

- 类名优先；
- 不使用深层级链式选择器；
- runtime 状态只用 `.active` / `.selected` 等明确 modifier；
- 新组件不要复用已经淘汰的旧 class 名。

### 29.3 覆盖策略

本次已经清理一部分第一套设计残留。以后不要继续采用：

```text
先写一整套旧设计 → 后面再写一整套新设计覆盖
```

正确方式：

```text
保留一个当前 source of truth；改版时直接修改 token / 当前组件规则；删除无引用旧 selector。
```

这能避免字体、间距、hover、responsive 在不同层发生隐式冲突。

---

## 30. 组件新增检查清单

新增任何 UI 组件前：

- [ ] 是否能复用现有 Section / card / range / select / export 样式？
- [ ] 字号是否来自现有语义级别？
- [ ] 间距是否使用 4/8/12/16/24/32/40/48？
- [ ] 是否使用 Open Sans？
- [ ] 是否使用现有 Ink / Muted / Line / Accent token？
- [ ] Hover / Selected / Focus 是否定义？
- [ ] 是否会遮挡 2D/3D 设计对象？
- [ ] 是否在 ≤1100px 和 ≤820px 仍可用？
- [ ] 是否把 UI 色误当成材料色？
- [ ] 是否引入新的制造术语而没有统一命名？

---

## 31. 当前设计规范摘要（可贴到开发任务顶部）

```text
FONT
Open Sans; fallback Arial/sans-serif
Weights 400 / 600 / 700 / 800

SPACING
4px base grid
4 / 8 / 12 / 16 / 24 / 32 / 40 / 48

CORE COLORS
Ink             #202226
Muted           #747980
Line            #C9CED8
Paper           #FFFFFF
Panel           #F7F8FA
Accent          #6379B7
Accent Soft     #DFE5F4
Control Surface #FAFBFC
Selected        #F8FAFF

LAYOUT
Desktop: workspace 72% / controls 28%, controls min 380px
Workspace: 3D 62% / print views 38%
≤1100: controls 360px
≤820: stacked layout

SECTION
12px gap / 16px padding
Header 12×16px
Section title 19.5px
Number badge 28×28px

CARD
3 columns
12px gap
min-height 112px
4px radius
Accent selected state

FORM
Select height 44px
Mode tab min-height 44px
Range group top 16px
Focus 2px accent + 2px offset

PRINT VIEW
canvas left / Part Colors right
24px gap
readout max-width 220px
Do not overlay readout on artwork
```

---

## 32. 版本控制原则

如果以后改视觉：

1. 先更新本设计规范；
2. 再改 CSS token / 当前组件；
3. 不在文件尾部追加第三套“覆盖式方案”；
4. 删除废弃 selector；
5. 做 Desktop 1440、1100、820 三个宽度回归；
6. 对比 Front Print / Back Print / Part Colors / 3D 是否发生非预期位移；
7. 视觉改动与材料/几何/导出代码分开 commit。

---

*This specification is derived from the current MilliHygro HTML implementation and is intended to be the source of truth for subsequent UI iterations.*
