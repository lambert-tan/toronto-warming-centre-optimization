# Toronto Warming Centre Capacity and Staffing Optimization

**Python | Monte Carlo Simulation | Integer Optimization | Decision Analytics**

Toronto warming centres can face sharp changes in demand during cold weather, while staffing, beds, and operating funds are limited. This project asks:

> **How should limited staffing and bed capacity be allocated across warming centres to reduce turn-aways under uncertain winter demand?**

## End-to-end workflow

1. Consolidate centre capacity and occupancy-based demand assumptions.
2. Convert average winter occupancy into centre-level arrival-rate inputs.
3. Simulate moderate and extreme-weather demand using Poisson arrivals.
4. Evaluate staffing requirements under physical-capacity and staff-ratio constraints.
5. Stress-test the operating plan over 5,000 simulated nights.
6. Compare equal, proportional, and targeted allocation of ten additional beds.
7. Test sensitivity to stronger extreme-weather demand.

## Main analytical idea

The project moves from **demand estimation** to **resource allocation** and then to **robustness testing**. Once staffing is sufficient to support the available beds, adding labour alone cannot remove the physical capacity ceiling. The analysis therefore extends the decision problem to bed allocation.

## Structure

```text
toronto-warming-centre-optimization/
├── README.md
├── requirements.txt
├── data/
│   └── processed/
│       └── centre_parameters.csv
├── notebooks/
│   └── warming_centre_end_to_end.ipynb
└── src/
    └── simulation.py
```

## Limitations

Occupancy is an imperfect proxy for unconstrained demand when centres are full. The Poisson arrival process, two-state weather model, and system-level transfer mechanism are simplifying assumptions. The results are therefore scenario-based analytical evidence rather than operational forecasts.

## Portfolio note

This is an independently rebuilt and extended portfolio version of an earlier academic team project. The workflow was reorganized and documented as a standalone analysis rather than presented as individual authorship of the original team submission.
