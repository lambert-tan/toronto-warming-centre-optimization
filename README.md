# ❄️ Toronto warming centres: staffing, beds and overnight referrals

In our graduate team’s extreme-weather planning scenario, **nine people were turned away while four beds remained unused**. Even a perfect transfer system could fill only four of those nine places. I wanted to know how much unmet demand planners might see across a winter, and how much the answer depends on which centres can take referrals.

Our team used integer optimization to allocate staff across seven sites. For this portfolio, I took that staffing plan as an input, rebuilt the demand simulation in Python and tested a change to the overnight transfer rule. The original planning results and my simulation answer different operational questions.

| Planning question | Evidence |
|---|---|
| Where can existing shifts cover more beds? | [Site-by-site allocation of 19 staff](results/staffing_results.csv) |
| How often does demand exceed the beds available that night? | [5,000-night Monte Carlo notebook and paired policy test](notebooks/warming_centre_end_to_end.ipynb) |
| Which ten-bed expansion did the team select? | [Original expansion comparison](results/capacity_expansion_results.csv) |

## Reading the staffing plan

The plan assigns **19 staff to 301 beds**. At one staff member per 20 clients, each centre has enough staff for its existing beds. For example, four staff at Elizabeth can support 80 clients, but the site has 75 beds. At that location, five additional beds could be staffed with the existing allocation. [Staffing by centre](results/staffing_results.csv)

| Original planning scenario | Demand | Admitted | Turned away | Reported operating cost |
|---|---:|---:|---:|---:|
| Moderate | 231 | 231 | 0 | $24,717 |
| Extreme | 306 | 297 | 9 | $32,795 |

Even if transfers could fill all four unused beds, at least five people would still lack a bed at this level of demand. The aggregate results do not explain why those four places went unused. The reported operating cost leaves $205 against the $33,000 budget, and the source table gives no cost breakdown to establish whether expansion is affordable. [Scenario results](results/scenario_results.csv) · [Cost assumptions](results/model_assumptions.csv)

![Physical beds and staffing capacity at each centre](assets/capacity_by_centre.svg)

## From one planning night to 5,000 simulated nights

The notebook holds staffing fixed and draws total arrivals for each 12-hour shift using centre-specific Poisson rates. Extreme nights have a 12% probability and a 10% increase in arrival rates. With seed 42, the simulation produced 574 extreme nights and averaged **17.0 turn-aways per extreme night**. The nine turn-aways above belong to a single planning scenario.

The transfer rule pools spare beds across all sites without a travel or intake limit. On moderate nights, two extreme-weather sites have zero local demand but their beds can still receive transfers in the simulation. This can understate unmet demand if those sites are closed. [Simulation notebook](notebooks/warming_centre_end_to_end.ipynb) · [Python implementation](src/simulation.py)

## What changes if closed sites cannot receive transfers?

I reran the transfer calculation on the **same simulated demand for each night**. On moderate nights, the alternative makes the 30 beds at Cecil and 30 at Jimmie Simpson unavailable for transfers. That leaves 241 beds across open sites. Extreme nights retain all 301 beds. Both versions still assume transfers between eligible sites are immediate.

| Open-site rule | Nights | Average turned away | 90th percentile turned away | Nights with anyone unserved |
|---|---:|---:|---:|---:|
| Moderate weather, five sites open | 4,426 | 3.0 | 12 | 1,314 (29.7%) |
| Extreme weather, seven sites open | 574 | 17.0 | 36 | 472 (82.2%) |

Under the original transfer rule the moderate-night average rounds to 0.0. Restricting transfers produces unmet demand on almost three in ten simulated moderate nights using exactly the same arrivals and staffing. For an operator, the immediate question is which receiving sites are open, staffed and able to accept a person at the time a referral is made. Across extreme nights, the 90th percentile of 36 also gives planners a clearer overflow scenario than the average alone. These are simulated turn-aways under the specified policies. [Reproduce the paired comparison](notebooks/warming_centre_end_to_end.ipynb)

## Where I would investigate expansion

The original expansion analysis identified a ten-bed allocation split between **Elizabeth (five) and Scarborough (five)**. At the assumed staffing ratio, Elizabeth can cover five additional beds and Scarborough can cover twelve. Both proposed additions therefore fit the existing shifts. The saved results do not give admissions by site for the alternative allocations. Before funding the expansion, I would ask for those comparisons and confirm which sites can accept transfers on each shift. [Expansion summary](results/capacity_expansion_results.csv)

There is a limit to what the simulation can establish about placement. With unrestricted transfers, nightly turn-aways depend on total demand and total effective beds. Any two expansions with the same staffed, open bed count yield the same total turn-aways on the same night. To decide *which site* should receive beds, I would compare transfer time, refused referrals and staffing by location. Those constraints can distinguish two allocations that look identical in the pooled model. The site recommendation above comes from the original planning study.

## Reproduce the stress test

```bash
pip install -r requirements.txt
jupyter notebook notebooks/warming_centre_end_to_end.ipynb
```

Run the cells in order to generate demand, check centre-level staffing capacity and simulate the fixed plan. The original solver and expansion runs are represented by their saved results.
