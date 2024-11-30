---
title: "Irreversible Fire Danger under Carbon Reduction"
categories: ["Irreversibility","Hysteresis","Fire"]
tags: ["Fire weather"]
description: ""
weight: 2
---

Fires emit a significant amount of CO<sub>2</sub> annually, which corresponds to ~20% of anthropogenic emissions. Recent increases in fire acitivities, marked by record-breaking fire events worldwide, raises concerns about a potential further surge in atmospheric CO<sub>2</sub> levels. To address these uncertainties in future CO<sub>2</sub> concentration, this study leverages climate model simulations to estimates future fire carbon emissions associated with enhanced fire weather. Furthermore, we assess whether/how effectively carbon reductions through neagative emissions could mitigate the heightened fire risk.


{{< toc >}}

## Key points
- In concentration-driven simulations, where wildfire emissions are often overlooked, the level of warming in future climates may have been underestimated.
- Once-elevated fire risk is not alleviated immediately by carbon removal due to the inertia of the climate system.
- Proper prevention and management plans are needed in order to successfully deliver the designed mitigation pathways.


## Methods
### Simulation

<div class="col-sm-4 portfolio-item shuffle-item">
  <a href="airseacouple"><img src="/files/research_figs/FWI_Figure1.png" alt=""></a>
</div>


We used CESM1.2 to simulate the climate status under
- Doubled CO<sub>2</sub> (year 2070), and  
- Reversed CO<sub>2</sub> (year 2210).
  
          

### Fire Weather Index


Fire weather index (FWI; Van Wagner, 1987) measures the degree of fire risk in terms of meteological conditions. It requires four daily variables: local noon-time near-surface temperature, wind speed, relative humidity, and 24-hour precipitation. 

Though simple, FWI can capture the actual fire activity (burned area, emission, etc.), with its high value significantly correlated with high fire emissions in wide areas over the globe. In other words, fire carbon emissions can be roughly estimated using weather variables.  

## Results

{{< mermaid class="text-center" >}}
graph LR;
    A(("**Climate Change**"))
    B(("**Fire Weather**"))
    C(("**Fire Activity**"))    
    D(("**Carbon Emissions**"))
    A --15% increase<br/>by doubling CO<sub>2</sub>--> B
    B --> C
    C --53% potential increase<br/>by doubling CO<sub>2</sub>--> D
    D --> A    

    style A fill:#d77,stroke:white,stroke-width:1px,color:#fff
    style B fill:#d77,stroke:white,stroke-width:1px,color:#fff
    style C fill:#d77,stroke:white,stroke-width:1px,color:#fff
    style D fill:#d77,stroke:white,stroke-width:1px,color:#fff


{{< /mermaid >}}

### How much CO<sub>2</sub>&nbsp;will be emitted from increased fires?

Our estimate suggests that fire danger will increase by approximately **15%** under doubled greenhouse gas (GHG) concentration. This, however, corresponds to about **53%** more fire emissions, since fire danger increases more in regions where fire activity is highly sensitive to weather conditions. 


### Even if we return the GHG level...

The heightened fire risk is projected to persist for a while (though with regional differences), and will not be immediately reversed to its previous level. Such prolonged high fire activity could continue to act as an additional source of GHG into the atmosphere.


## Implications

<div class="col-sm-4 portfolio-item shuffle-item">
  <img src="/files/research_figs/FWI_Figure2.png" alt="">
</div>


Without proper management practices, increased fires could significantly disrupt the intended emission pathways, both globally and locally. 

For instance, in the countries shown on the left, additional fire emissions inferred from prolonged fire risks could amount to 13-54% of their current fire emissions; i.e., more attention should be paid to fire management in controlling their national GHG inventories.

Shown on the right are countries where GHG reduction could lead to a substantial decrease in fire-related emissions; The total fire carbon reduction effect in these 10 countries (1.35 Pg/yr) is comparable to that of all other countries combined (1.44 Pg/yr). These countries can thus be regarded as key regions for global co-benefits in accelerating the reduction of GHG levels.


## Publication

Kim, H.-J. and J.-S. Kim, S.-I. An, J. Shin, J.-H. Oh, and J.-S. Kug, Pervasive fire danger continued under a negative emission scenario, 2024, *Nature Communications* **15** 11010. doi:[https://doi.org/10.1038/s41467-024-54339-2](https://doi.org/10.1038/s41467-024-54339-2)

