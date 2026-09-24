# Toronto Warming Centre Capacity and Staffing Optimization

**Python | Monte Carlo Simulation | Integer Optimization | Decision Analytics**

Toronto warming centres operate under a practical resource-allocation problem: demand rises during severe cold, but beds, staff, and operating funds are limited. This project examines how staffing and physical capacity can be allocated across seven warming centres while keeping nightly operations within a **$33,000 budget**.

> **Business question:** How should limited staffing and bed capacity be allocated across Toronto warming centres to reduce turn-aways under uncertain winter demand?

## Project Overview

The analysis follows three stages. First, centre-level demand is represented with Poisson arrivals under moderate and extreme-weather conditions. Second, an optimization model allocates staff subject to physical capacity, staffing, and budget constraints. Third, the operating plan is stress-tested through Monte Carlo simulation to examine how it performs when realized demand differs from expected demand.

The portfolio version extends the original analysis by separating the modelling workflow into reproducible Python components and GitHub-readable result files.

## Key Results

The optimization allocates **19 staff across seven warming centres**. At a 1:20 staff-to-client ratio, this staffing level can theoretically support 380 clients, compared with only **301 physical beds** across the network.

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

The Excel optimization results show a clear difference between the two planning scenarios:

| Scenario | Demand | Admitted | Turn-aways | Operating Cost |
|---|---:|---:|---:|---:|
| Moderate | 231 | 231 | 0 | $24,717 |
| Extreme | 306 | 297 | 9 | $32,795 |

Under the moderate scenario, expected demand can be accommodated without turn-aways. Under the extreme scenario, demand rises to 306 while the system admits 297 clients, leaving 9 turn-aways. The extreme-weather operating cost remains just below the $33,000 nightly budget.

The staffing calculation also points to an important operational constraint. With 19 staff, staffing-supported capacity exceeds the number of available beds. Under the assumptions used here, this shifts the resource question from simply adding labour toward determining whether additional physical capacity would reduce unmet demand.

## Methodology

The workflow is organized around four analytical steps:

1. **Demand modelling:** Convert centre-level occupancy assumptions into hourly arrival rates and simulate demand using a Poisson process.
2. **Staffing optimization:** Allocate staff while accounting for the 1:20 staff-to-client ratio, physical capacity, operating costs, and the $33,000 nightly budget.
3. **Stress testing:** Evaluate the operating plan over 5,000 simulated nights rather than relying only on expected demand.
4. **Capacity analysis:** Examine whether adding beds provides greater value once staffing is sufficient to support existing physical capacity.

## Model Assumptions

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

These assumptions are modelling inputs rather than forecasts. They are retained to make the optimization logic transparent and reproducible.

## Repository Structure

```text
toronto-warming-centre-optimization/
├── README.md
├── requirements.txt
├── data/
│   └── processed/
│       └── centre_parameters.csv
├── notebooks/
│   └── warming_centre_end_to_end.ipynb
├── results/
│   ├── staffing_results.csv
│   ├── scenario_results.csv
│   └── model_assumptions.csv
└── src/
    └── simulation.py
```

The `results/` folder contains GitHub-readable extracts of the original Excel optimization outputs so that the main model results can be reviewed without opening the workbook.

## Limitations

Occupancy is an imperfect proxy for unconstrained demand when a centre is already full. The Poisson arrival process, two-state weather model, and transfer assumptions simplify actual shelter demand and operations. The results should therefore be interpreted as scenario-based decision support rather than operational forecasts.

The optimization results also depend on the cost, utility, and penalty assumptions specified above. Different assumptions could change the preferred allocation.

## Portfolio Note

This repository is an independently rebuilt and extended portfolio version of an earlier academic team project. The workflow has been reorganized and documented as a standalone analysis. It is not presented as individual authorship of the original team submission.
