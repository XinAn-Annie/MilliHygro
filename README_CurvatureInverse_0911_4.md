# MilliHygro 0911_4 · Curvature Inverse

## Online demo

The deployed GitHub Pages site is available at [https://xinan-annie.github.io/MilliHygro/](https://xinan-annie.github.io/MilliHygro/). It is published from the root of the `main` branch through `index.html`.

## What changed

`MilliHygro_0911_4_CurvatureInverse.html` adds an inverse design step to the existing UI. For each editable region, the user selects a CMYK color (which sets the concentration sum), enters the required absolute curvature, and chooses which face has more toner. The tool then calculates the required front/back concentration allocation and updates the print previews.

The previous UI file, `MilliHygro_0911_3_UIRefined.html`, is unchanged.

## Fitted model

The embedded model is ported from:

`mechanisms/第二版本的三维浓度和-浓度差热力图/绘图脚本.py`

It uses the same constrained PCHIP response surface and 2%-spaced calculation grid:

```text
|κ| = F(Csum, |ΔC|)
Csum = Cf + Cb
ΔC = Cb - Cf
```

where:

- `Cf` is the front-face concentration (%).
- `Cb` is the back-face concentration (%).
- `Csum` and `|ΔC|` are percentages.
- `|κ|` is absolute curvature in mm⁻¹.
- Valid domain: `0 ≤ |ΔC| ≤ Csum ≤ 400%`.
- Embedded global range: `0 ≤ |κ| ≤ 1.3733 mm⁻¹`.

The fitted surface contains no negative curvature. Bend direction is therefore represented independently in the UI by **More toner: Front / Back**. This choice swaps `Cf` and `Cb` and supplies the sign used only by the 3D deformation preview; it does not change the fitted magnitude.

## Inverse calculation

For the current `Csum`, the tool finds `|ΔC|` by bisection on the monotonic fitted surface. It then calculates:

```text
Higher toner on Front:
Cf = (Csum + |ΔC|) / 2
Cb = (Csum - |ΔC|) / 2

Higher toner on Back:
Cf = (Csum - |ΔC|) / 2
Cb = (Csum + |ΔC|) / 2
```

The maximum selectable curvature is recalculated from the active region's `Csum`. Values outside the fitted range are clamped to the valid boundary.

For Solid and Density modes, `Csum` is the sum of the selected CMYK channels. For Gradient mode, the present implementation uses the larger CMYK sum of the two endpoints as the representative `Csum` for inverse calculation.

## Validation

- JavaScript/Python forward-surface comparison: maximum error about `1.1 × 10⁻¹⁶ mm⁻¹` over the checked source and interpolated points.
- Inverse then forward evaluation: maximum error about `1.8 × 10⁻¹³ mm⁻¹` over the checked cases.
- UI regression checks cover exact curvature entry, zero/negative input handling, fitted-range limits, and Front/Back concentration swapping.

## Interpretation boundary

The Python source describes these as user-confirmed, trend-constrained plotting data rather than a replacement for archived raw measurements. The inverse output should therefore be treated as a design estimate within the fitted domain, not as validated extrapolation outside it.
