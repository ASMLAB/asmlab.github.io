---
title: "Current-wind interaction in the Kuroshio extension"
categories: ["modeling","MITgcm", "WRF"]
tags: ["modeling"]
description: ""
weight: 2
---
Relative wind (RW; wind relative to surface currents) has been shown to play a crucial role in air-sea interactions, influencing both atmospheric and oceanic dynamics. While the RW effects through momentum flux are well-documented, those through turbulent heat fluxes remain unknown. In this study, we investigate two distinct surface current feedbacks – those associated with the momentum flux and turbulent heat fluxes – by modifying respective bulk formulations in the regional ocean-atmosphere coupled system, and analyze both immediate and seasonal changes in the boundary layers.

{{< toc >}}

## Key points
- Surface currents modify the lower atmosphere and upper ocean through air-sea fluxes.
- Surface current response to air-sea fluxes depends on wind-current angle and speed.
- Surface current coupling can alter the Kuroshio Current and Extension seasonally.

## Numerical simulation
### Ocean-atmosphere coupled system
In this study, we investigated the effect of current coupling using the regional coupled ocean-atmosphere model, namely, Scripps-KAUST Regional Integrated Prediction System (SKRIPS) v1.2. In this model, the ocean model, MITgcm, and atmosphere model, WRF, are combined through the ESMF.
WRF transmits the following data to the MITgcm: 2-m specific humidity, 2-m air temperature, 10-m wind, moisture flux, precipitation, surface pressure, and surface heat fluxes. In return, MITgcm transmits the SST and surface current data to WRF.

### Wind stress and turbulent heat flux
To identify the effect of current-wind interaction, we modify the bulk formulations of air-sea momentum and turbulent heat flux.
To exclude the effect of surface currents from wind stress and heat flux calculations, we used the absolute wind as a 10-m wind input to the bulk formula. Subsequently, by modifying the bulk formation of turbulent heat fluxes to use the absolute wind in the friction velocity, the effect of surface currents on the turbulent heat flux can be eliminated. We conducted three experiments:
<div class="col-sm-4 portfolio-item shuffle-item">
  <a href="exp_cases"><img src="/files/research_figs/exp_cases.png" alt=""></a>
</div>

## Results
Surface currents modulate the air-sea fluxes that alter the low-level atmosphere and upper ocean. Initially, the responses to surface currents depend on the wind-
current angle and surface current speed. In a seasonal timescale, the current feedbacks can alter the position and speed of the Kuroshio Extension and eddies.

{{< mermaid class="text-center" >}}
---
config:
  look: handDrawn
  theme: neutral
---
flowchart LR
A[Surface current coupling] --> B{Surface current speed
Wind-current angle}
B --> |Immediately| C[Wind stress,
low level wind speed,
surface current speed]
B --> |Immediately| D[Turbulent heat flux,
low level temperature and humidity]
C --> |Seasonally|E[Changes in oceanic background states]
D --> |Seasonally|E
{{< /mermaid >}}

## Application
This study indicate the importance of mesoscale oceanic forcing near the western boundary currents in terms of two types of current feedbacks.

## Publication
Cho, A. and H. Song, H. Seo, R. Sun, M.R. Mazloff, A.C. Subramanian, B.D. Cornuelle and A.J. Miller, Dynamic and thermodynamic coupling between the atmosphere and ocean near the Kuroshio current and extension system, 2025, *Ocean Modelling*, **194** 102496, https://doi.org/10.1016/j.ocemod.2024.102496
