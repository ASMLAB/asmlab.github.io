---
title: "Top-down and Bottom-up Mixing within the Ocean Mixed Layer"
categories: ["modeling","PALM"]
tags: ["modeling","Large Eddy Simulation"]
description: ""
weight: 2
---

In the ocean, phytoplankton can grow in the euphotic zone, resulting in high concentrations near the sea surface. During the autumn, the ocean's upper layer lacks nutrients, as most of the nutrients supplied by winter mixing are depleted because already used in the summer, leaving nutrients concentrated in the lower layers. Without vertical motion, phytoplankton near the sea surface are hard to grow in such conditions. However, as the stratification weakens and the mixed layer depth (MLD) begins to deepen in the autumn, nutrients can be entrained into the MLD and supplied to the upper layers, potentially triggering an autumn phytoplankton bloom. In this study, the occurrence and characteristics of the autumn phytoplankton bloom were simulated and investigated using a Large Eddy Simulation coupled with a Lagrangian plankton model.


{{< toc >}}

## Key points
- mixing of top-down and bottom-up diffusing tracers in the mixed layer is investigated using Large Eddy Simulation coupled to a Largrangian plankton model
- The effect of heterogeneity in phytoplankton and nutrient concentration distributions on phytoplankton production is investigated 
- A simple box plankton model is proposed to predict an autumn phytoplankton bloom by considering the mixing process of tracers

## Numerical simulation
### Configuration
The idealized Autumn conditions are simulated using PALM, where the upper layer was rich in phytoplankton and the lower layer is abundant in nutrients, for investigate the autumn phytoplankton bloom.

<div class="col-sm-4 portfolio-item shuffle-item">
  <img src="/files/research_figs/autumnbloom_fig1.jpg" class="img-responsive; width:10%;" alt="">
</div>

## Results
### Heteogeneity of the phytoplankton and nutrient concentration
Phytoplankton are transported downwards from the sea surface, while nutrients transported upwards from the base of the mixed layer, resulting in spatial heterogeneity unlike an ideal perfectly mixed layer.

<div class="col-sm-4 portfolio-item shuffle-item">
  <img src="/files/research_figs/autumnbloom_fig2.jpg" class="img-responsive; width:25%;" alt="">
</div>

### A simple box model using reduction ratio
To correct for the ideal mixed layer and the heterogeneity present in reality, a reduction ratio was applied to investigate the differences in the occurrence of the autumn bloom.

<div class="col-sm-4 portfolio-item shuffle-item">
  <img src="/files/research_figs/autumnbloom_fig3.jpg" class="img-responsive; width:25%;" alt="">
</div>

## Application
This study analyzed the effects of various conditions on the heterogeneity of phytoplankton and nutrients. By investing the reduction ratio for predicting the autumn phytoplankton bloom, it was shown using a simple box plankton model that considering heterogeneity could lead to a reduction in the bloom's amplitude or even inhibit the occurrence of the bloom. This study emphasizes the need for further research under more realistic conditions to improve the autumn phytoplankton bloom predictions.

## Publication
Noh,Y., Seunu, H.J., Song, H., and Choi, Y.(2024). Mixing of top-down and bottom-up diffusing reactive tracers within the ocean mixed layer and its application to autumn phytoplankton blooms. *Journal of Geophysical Research: Oceans*, **129**, e2024JC021757. https://doi.org/10.1029/2024JC021757