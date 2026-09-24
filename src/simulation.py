"""Reusable simulation functions for the warming-centre portfolio project."""
import numpy as np
import pandas as pd

def evaluate_policy(centres, capacity, staff, hours_open=12, extreme_prob=.12,
                    staff_ratio=20, n=5000, seed=42):
    rng = np.random.default_rng(seed)
    records = []
    for night in range(n):
        extreme = rng.random() < extreme_prob
        total_demand = total_local_served = total_overflow = total_vacancy = 0
        for _, r in centres.iterrows():
            if (not extreme) and r["extreme_only"]:
                demand = 0
            else:
                mult = 1.10 if extreme else 1.0
                demand = rng.poisson(r["arrival_rate"] * hours_open * mult)
            eff_cap = min(capacity[r["centre"]], staff[r["centre"]] * staff_ratio)
            total_demand += demand
            total_local_served += min(demand, eff_cap)
            total_overflow += max(demand - eff_cap, 0)
            total_vacancy += max(eff_cap - demand, 0)
        transferred = min(total_overflow, total_vacancy)
        turnaways = total_overflow - transferred
        served = total_local_served + transferred
        records.append({
            "night": night + 1,
            "scenario": "Extreme" if extreme else "Moderate",
            "demand": total_demand,
            "served": served,
            "transferred": transferred,
            "turnaways": turnaways,
            "service_level": served / total_demand if total_demand else 1.0
        })
    return pd.DataFrame(records)
