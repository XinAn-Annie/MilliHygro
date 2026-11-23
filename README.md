# MilliHygro · Curvature Inverse

MilliHygro 是一个用于双面 CMYK 浓度分配与曲率反求的交互式设计工具。用户可以导入 SVG 或 PNG 图形，编辑区域颜色、浓度和曲率，并在 2D 预览与 3D 形变预览之间切换。

## 在线体验

**GitHub Pages：** [https://xinan-annie.github.io/MilliHygro/](https://xinan-annie.github.io/MilliHygro/)

页面由 `main` 分支根目录的 `index.html` 提供，GitHub Pages 会自动发布最新提交。

## 项目文件

- `index.html`：当前网页入口及主要交互逻辑。
- `assets/`：Three.js、OrbitControls 和 PNG 图层处理依赖。
- `make_svg.py`：SVG 资源生成脚本。
- `README_CurvatureInverse_0911_4.md`：拟合模型、反求计算和验证说明。
- `MilliHygro_Web_Design_Specification.md`：网页视觉与交互设计规范。

## 本地运行

可直接打开 `index.html` 预览；如果浏览器限制本地文件资源访问，可在项目目录启动静态服务器后访问 `http://localhost:8000/`。

## 计算说明

工具根据 CMYK 总浓度 `Csum` 和正反面浓度差 `|ΔC|` 的拟合曲面反求目标曲率，并根据“Front / Back”选项分配正反面浓度。当前版本还支持带图层 PNG 的 SVG 导入、关联 PNG 文件和每个图层的正反面透明度控制。计算结果应作为拟合域内的设计估计使用，详细模型与验证边界见 [README_CurvatureInverse_0911_4.md](README_CurvatureInverse_0911_4.md)。

## 发布信息

- 仓库：[XinAn-Annie/MilliHygro](https://github.com/XinAn-Annie/MilliHygro)
- Pages 地址：[https://xinan-annie.github.io/MilliHygro/](https://xinan-annie.github.io/MilliHygro/)
- 发布分支：`main`
- 发布目录：`/`
