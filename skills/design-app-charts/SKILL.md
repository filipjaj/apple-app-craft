---
name: design-app-charts
description: "Design or implement Apple app charts with Swift Charts, including function/vectorized plots, scales and accessible meaning. Use for chart communication and rendering, not general dashboards."
---

# Design App Charts

## Goal

Communicate the intended data comparison accurately and legibly at the app’s real data volume.

## Working context

Inspect the actual app, SDK, deployment targets and project conventions. For framework details, resolve the library with Context7 and query the relevant concept; use current official Apple documentation when coverage is incomplete. Read [source lessons](references/source-lessons.md) for timestamped decisions and provenance. Preserve the user’s product direction, supported systems and working behavior.

## Workflow

1. Define the question the chart should answer, units, series and data quality. Choose a representation appropriate to comparison, distribution or change; do not add a chart merely because the data is numeric.

2. Set domains, scales and sampling intentionally. Restrict function plots to meaningful valid input and handle undefined, nonfinite or missing values. Do not let a cropped scale or implicit baseline misrepresent the comparison.

3. Choose ordinary versus vectorized/function representations based on supported SDK, data volume and measured rendering cost. Keep preparation outside repeated view work and retain representative accuracy when sampling or aggregation is necessary.

4. Provide readable labels, units, legends and selection feedback with accessible alternatives for essential values. Preserve distinguishability without relying only on color and verify small layouts and localized formatting.

5. Check real and extreme datasets, scale changes and performance on the supported target. Explain any aggregation or omitted values and compare the displayed conclusion with the underlying data.

## Verify the outcome

- The chart answers the intended question without scale distortion.
- Invalid values and real data volume have deliberate handling.
- Essential meaning is accessible without color alone.

## Deliverable

Leave the requested implementation, design or prioritized review. Explain the resulting behavior, relevant compatibility choices, performed checks and remaining limits. Preserve the project’s required testing tools, including SwiftProbe when configured. Distinguish source inspection, previews, actual device interaction and measured behavior.
