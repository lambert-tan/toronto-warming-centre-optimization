# Toronto Warming Centre Capacity and Staffing Optimization

> **How should limited staffing and bed capacity be allocated across Toronto warming centres when winter demand is uncertain?**

**Python · Monte Carlo Simulation · Integer Optimization · Decision Analytics**

This project models nightly resource allocation across seven Toronto warming centres. The objective is to reduce unmet demand while staying within a **$33,000 operating budget** and respecting staffing and physical-capacity constraints.

## Results at a glance

**7 centres · 19 staff · 301 physical beds · 5,000-night stress test**

- The optimized staffing plan supports up to **380 clients**, compared with **301 physical beds**.
- Under the moderate planning scenario, **231 of 231** clients are admitted.
- Under the extreme scenario, demand rises to **306** and **297** clients are admitted, leaving **9 turn-aways**.
- Extreme-scenario operating cost is **$32,795**, below the **$33,000** nightly budget.
- Once staffing capacity exceeds available beds, physical capacity becomes the tighter constraint.

<p align="center"><img src="assets/scenario_comparison.svg" width="850" alt="Moderate and extreme demand scenarios"></p>

## Capacity decision

With 19 staff, staffing-supported capacity exceeds the number of available beds. Additional staff therefore do not increase admissions once physical capacity is reached.

The next stage of the analysis compares how **10 additional beds** could be allocated. In the original expansion analysis, the targeted configuration placed **5 beds at Elizabeth and 5 at Scarborough**. Under the model assumptions, this configuration was reported to improve welfare by **5.7%** and reduce turn-aways by **67%** relative to the comparison setting used in the original analysis.

These are scenario-based model results rather than forecasts of actual shelter outcomes.

<p align="center"><img src="assets/decision_workflow.svg" width="850" alt="Decision workflow from demand to targeted capacity"></p>

## Capacity bottleneck

The optimization allocates **19 staff** across the seven centres. At a **1:20 staff-to-client ratio**, this staffing level can support 380 clients, while the network contains 301 physical beds.

| Centre | Staff | Physical Capacity | Staff-Supported Capacity |
|---|---:|---:|---:|
| Elizabeth | 4 | 75 | 80 |
| George | 2 | 30 | 40 |
| Scarborough | 4 | 68 | 80 |
| North York | 3 | 46 | 60 |
| Spadina | 2 | 22 | 40 |
| Cecil | 2 | 30 | 40 |
| Jimmie Simpson | 2 | 30 | 40 |
| **Total** | **19** | **301** | **380** |

<p align="center"><img src="assets/capacity_by_centre.svg" width="850" alt="Physical versus staff-supported capacity by centre"></p>

Once staffing-supported capacity is above the bed count, additional staffing alone cannot increase the number of clients admitted.

## Scenario results

| Scenario | Demand | Admitted | Turn-aways | Operating Cost |
|---|---:|---:|---:|---:|
| Moderate | 231 | 231 | 0 | $24,717 |
| Extreme | 306 | 297 | 9 | $32,795 |

The moderate scenario can be served without turn-aways. In the extreme scenario, demand exceeds available capacity even though operating cost remains within budget.

## Analytical workflow

The analysis combines deterministic optimization with stochastic stress testing:

1. **Demand modelling** — represent centre-level demand using Poisson arrivals under moderate and extreme weather conditions.
2. **Staffing optimization** — allocate staff subject to physical capacity, staffing ratios, operating costs, and the nightly budget.
3. **Monte Carlo stress test** — evaluate the operating plan over **5,000 simulated nights**.
4. **Capacity expansion analysis** — compare additional-bed allocation strategies once staffing is no longer the main constraint.

## Stress testing

The optimized plan is based on expected planning conditions, while realized demand varies from night to night. The **5,000-iteration Monte Carlo simulation** tests how the staffing plan performs under that variation.

Under high demand, simulated outcomes can still reach the physical bed ceiling. This is why the expansion stage focuses on bed allocation rather than simply increasing staffing.

## Model assumptions

| Parameter | Value |
|---|---:|
| Nightly budget | $33,000 |
| Staff-to-client ratio | 1:20 |
| Staff cost per 12-hour shift | $312 |
| Operating cost per admitted client | $107 |
| Transfer cost | $147 |
| Moderate-weather probability | 88% |
| Extreme-weather probability | 12% |
| Admission utility | $500 |
| Transfer disutility | $50 |
| Turn-away penalty | $2,000 |

These are modelling inputs rather than forecasts. Different assumptions can change the preferred allocation.

## Repository structure

```text
toronto-warming-centre-optimization/
├── assets/
│   ├── capacity_by_centre.svg
│   ├── decision_workflow.svg
│   └── scenario_comparison.svg
├── data/
│   └── processed/
│       └── centre_parameters.csv
├── notebooks/
│   └── warming_centre_end_to_end.ipynb
├── results/
│   ├── capacity_expansion_results.csv
│   ├── model_assumptions.csv
│   ├── scenario_results.csv
│   ├── staffing_results.csv
│   └── stage3_stress_test_summary.csv
├── src/
│   └── simulation.py
├── requirements.txt
└── README.md
```

The `results/` folder contains the main model outputs in CSV format so they can be reviewed directly on GitHub.

## Limitations

This is a scenario-based decision model. Occupancy is an imperfect proxy for unconstrained demand when centres are already full. The Poisson process, two-state weather assumption, transfer logic, and cost structure also simplify real operations.

The capacity-expansion results should be interpreted as model-based comparisons under the stated assumptions, not as predictions of actual shelter performance.

## Portfolio note

This repository is an independently rebuilt and extended portfolio version of an earlier academic team project. The workflow has been reorganized and documented as a standalone analysis and is not presented as individual authorship of the original team submission.

---

**Lambert Tan**  
Master of Management in Analytics · Smith School of Business, Queen's University
