---
title: "IOD&ENSO"
categories: ["modeling","MITgcm"]
tags: ["modeling"]
description: ""
weight: 2
---
The variabilities in the tropical climate are accompanied by changes in tropical deep convection, which can influence the atmospheric circulation in the Southern Hemisphere (SH). We investigate the processes and results of the teleconnection between the tropics and extratropics in the Southern Hemisphere.

{{< toc >}}

## Key points
- Indian Ocean Dipole (IOD)’s Rossby wave train is partially similar to the climatology; a negative IOD enormously increases zonal wavenumber 3
- IOD (El Niño Southern Oscillation, or ENSO) is negatively (positively) correlated with zonal wavenumber 2 and 3 (1) in austral spring
- The extremely positive IOD in 2019 exhibited more significant increases and unusual changes in wave patterns

### methodology
The research period is SON (September-November) when the response of the Southern Hemisphere atmosphere to the IOD and ENSO is significant. Despite their high correlation with each other, their individual influences are clearly analyzed using partial regression. The Dipole Mode Index (DMI), which shows the strength of IOD, is defined as the difference in the averaged SST anomaly between the western (50°E−70°E, 10°S−10°N) and the eastern tropical region (90°E−110°E, 10°S−0°S). ENSO is represented by the Oceanic Niño Index (ONI), which is defined as the 3-month running mean of SST over the tropical Pacific (5°S−5°N, 170°W−120°W). The zonal wavenumber (ZWN) is calculated by performing a Fourier Transform on the atmospheric fields zonally.


### Results

We found that the Rossby wave train of the IOD is similar to the climatological wave pattern in the figure below.
<div class="col-sm-4 portfolio-item shuffle-item">
  <img src="/files/research_figs/Figure_wave.png" class="img-responsive; width:25%;" alt="">
</div>

The total process seems to be in the link below.
{{< mermaid class="text-center" >}}
graph LR

    subgraph   
        A(Positive IOD)
        B(El Niño)
    end

    A --> C(Eastward wave propagation)
    B --> D(Southward wave propagation)
    C --> E(Resembling climatological pattern)
    
    subgraph  
        G(Significantly decreased ZWN3)
        H(Increased ZWN1)
    end

	D --> H
    E --> G
    G --> I(Affecting the atmosphere and sea ice)
    H --> I

{{< /mermaid >}}

The negative phase of them seems to lead to opposite responses.

## Application
We explored the teleconnection between IOD/ENSO and the extratropics in the Southern Hemisphere. As the intensity and frequency of IOD events are predicted to increase in a warming climate, extreme weather patterns are expected to be more frequent due to teleconnections.

## Publication
Kim, D., H. Song, H.-Y. Chun, C. Yoo, M.-J. Kang and H.-K. Lee (2024): Springtime Southern Hemisphere Quasi-Stationary Planetary Wave Activities Associated With ENSO/IOD. *Journal of Geophysical Research: Atmospheres*, **129**, e2023JD039678. 
https://doi.org/10.1029/2023JD039678"