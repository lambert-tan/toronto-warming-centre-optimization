# Toronto Warming Centre Capacity and Staffing

On an extreme-weather night, the original Toronto planning scenario admitted 297 of 306 people. With 301 physical beds across seven sites, **four beds remained unused while nine people were turned away**. That gap raises two distinct planning questions: where would more beds help, and could the network use more of the beds it already has?

Our graduate team developed the staffing plan through integer optimization. For this portfolio, I rebuilt the demand simulation in Python and tested that fixed plan over 5,000 nights. [Original scenario results](results/scenario_results.csv)

## The planning decision

The plan assigns **19 staff to 301 beds**. At one staff member per 20 clients, each centre has enough staff for its existing beds. For example, four staff at Elizabeth can support 80 clients, but the site has 75 beds. At that location, five additional beds could be staffed with the existing allocation. [Staffing by centre](results/staffing_results.csv)

| Original planning scenario | Demand | Admitted | Turned away | Reported operating cost |
|---|---:|---:|---:|---:|
| Moderate | 231 | 231 | 0 | $24,717 |
| Extreme | 306 | 297 | 9 | $32,795 |

Even if transfers could fill all four unused beds, at least five people would still lack a bed at this level of demand. The aggregate results do not explain why those four places went unused. The reported operating cost leaves $205 against the $33,000 budget, and the source table gives no cost breakdown to establish whether expansion is affordable. [Scenario results](results/scenario_results.csv) · [Cost assumptions](results/model_assumptions.csv)

![Physical beds and staffing capacity at each centre](assets/capacity_by_centre.svg)

## Stress test across 5,000 nights

The notebook holds staffing fixed and draws total arrivals for each 12-hour shift using centre-specific Poisson rates. Extreme nights have a 12% probability and a 10% increase in arrival rates. With seed 42, the simulation produced 574 extreme nights and averaged **17.0 turn-aways per extreme night**. The nine turn-aways above belong to a single planning scenario.

The transfer rule pools spare beds across all sites without a travel or intake limit. On moderate nights, two extreme-weather sites have zero local demand but their beds can still receive transfers in the simulation. This can understate unmet demand if those sites are closed. [Simulation notebook](notebooks/warming_centre_end_to_end.ipynb) · [Python implementation](src/simulation.py)

## Where additional beds could help

The original expansion analysis identified a ten-bed allocation split between **Elizabeth (five) and Scarborough (five)**. At the assumed staffing ratio, Elizabeth can cover five additional beds and Scarborough can cover twelve. Both proposed additions therefore fit the existing shifts. The saved results do not give admissions by site for the alternative allocations. Before funding the expansion, I would ask for those comparisons and confirm which sites can accept transfers on each shift. [Expansion summary](results/capacity_expansion_results.csv)

## Reproduce the stress test

```bash
pip install -r requirements.txt
jupyter notebook notebooks/warming_centre_end_to_end.ipynb
```

Run the cells in order to generate demand, check centre-level staffing capacity and simulate the fixed plan. The original solver and expansion runs are represented by their saved results.
