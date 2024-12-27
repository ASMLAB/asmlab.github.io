---
title: "Meridional Wind on the Southern Ocean"
categories: ["modeling","MITgcm"]
tags: ["modeling"]
description: ""
weight: 2
---

Antarctica experiences strong katabatic winds, which are powerful enough to drive sea ice away from the coastline. However, there remains significant uncertainty regarding the strength of these winds and their influence on Southern Ocean circulation. In this study, we investigate the responses of Antarctic sea ice and ocean circulation to southerly wind perturbations.

{{< toc >}}

## Key points
- The southerly wind anomaly over the Antarctic seasonal ice zone enhances the seasonality of sea ice extent and volume.
- Southerly wind anomalies increase buoyancy loss at leads and polynyas, and strengthen the lower meridional overturning circulation cell. 
- Northerly wind anomalies result in opposite responses in the seasonality of the sea ice volume, ocean states and lower cell. 

## Numerical simulation
### Configuration
The idealized channel configuration is prepared in MITgcm to represent the Southern Ocean and Antarctic sea ice, which captures both temperature and salinity fields as well as the meridional overturning circulation.
<div class="col-sm-4 portfolio-item shuffle-item">
  <a href="airseacouple"><img src="/files/research_figs/fig2_TS_snap_v2.png" alt=""></a>
</div>

### Perturbations on the meridional wind
We perturbed the meridional wind by either adding or reducing 1 m/s near the south pole, which gradually approaches zero near roughly 62S.

### Results
It seems that the link below is at work.
{{< mermaid class="text-center" >}}
graph LR
    A(stronger southerly wind) --> B(increased leads and polynyas)
    B --> C(stronger lower cell)
    C --> E(enhanced upwelling of warmer water)
    E --> F(shrinking summertime sea ice edge)
    A --> D(larger sea ice extent in winter)
    F --> G(greater sea ice seasonality)
    D --> G
{{< /mermaid >}}
The weaker southerly wind anomalies seem to lead to the opposite responses.

## Application
The southerly winds over Antarctica have relatively high uncertainty, exhibiting significant variability across atmospheric reanalysis products. Future changes in these winds introduce an additional layer of uncertainty. This study emphasizes the critical link between southerly winds over the sea ice and the circulation of the Southern Ocean, underscoring the need for greater efforts to improve the accuracy of southerly wind estimates to enhance the reliability of Southern Ocean circulation simulations.

## Publication
Song, H. and Y. Choi, E.W. Doddridge and J. Marshall, The Responses of Antarctic sea ice and overturning cells to meridional wind forcing, Journal of Climate, sub judice
