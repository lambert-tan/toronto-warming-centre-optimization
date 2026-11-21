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

## What changes if closed sites cannot receive transfers?

I reran the transfer calculation on the **same simulated demand for each night**. On moderate nights, the alternative makes the 30 beds at Cecil and 30 at Jimmie Simpson unavailable for transfers. That leaves 241 beds across open sites. Extreme nights retain all 301 beds. Both versions still assume transfers between eligible sites are immediate.

| Open-site rule | Nights | Average turned away | 90th percentile turned away | Nights with anyone unserved |
|---|---:|---:|---:|---:|
| Moderate weather, five sites open | 4,426 | 3.0 | 12 | 1,314 (29.7%) |
| Extreme weather, seven sites open | 574 | 17.0 | 36 | 472 (82.2%) |

Under the original transfer rule the moderate-night average rounds to 0.0. Restricting transfers produces unmet demand on almost three in ten simulated moderate nights using exactly the same arrivals and staffing. For an operator, the immediate question is which receiving sites are open, staffed and able to accept a person at the time a referral is made. Across extreme nights, the 90th percentile of 36 also gives planners a clearer overflow scenario than the average alone. These are simulated turn-aways under the specified policies. [Reproduce the paired comparison](notebooks/warming_centre_end_to_end.ipynb)

## Where additional beds could help

The original expansion analysis identified a ten-bed allocation split between **Elizabeth (five) and Scarborough (five)**. At the assumed staffing ratio, Elizabeth can cover five additional beds and Scarborough can cover twelve. Both proposed additions therefore fit the existing shifts. The saved results do not give admissions by site for the alternative allocations. Before funding the expansion, I would ask for those comparisons and confirm which sites can accept transfers on each shift. [Expansion summary](results/capacity_expansion_results.csv)

There is a limit to what the simulation can establish about placement. With unrestricted transfers, nightly turn-aways depend on total demand and total effective beds. Any two expansions with the same staffed, open bed count yield the same total turn-aways on the same night. To decide *which site* should receive beds, I would compare transfer time, refused referrals and staffing by location. Those constraints can distinguish two allocations that look identical in the pooled model. The site recommendation above comes from the original planning study.

## Reproduce the stress test

```bash
pip install -r requirements.txt
jupyter notebook notebooks/warming_centre_end_to_end.ipynb
```

Run the cells in order to generate demand, check centre-level staffing capacity and simulate the fixed plan. The original solver and expansion runs are represented by their saved results.
