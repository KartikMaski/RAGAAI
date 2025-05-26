# === analysis_agent.py ===
def calculate_exposure(asia_holdings: dict, total_aum: float):
    asia_value = sum(asia_holdings.values())
    percent = (asia_value / total_aum) * 100
    return {
        "asia_value": round(asia_value, 2),
        "total_aum": round(total_aum, 2),
        "asia_exposure_percent": round(percent, 2)
    }

def analyze_risk(position_changes: dict):
    high_risk = [k for k, v in position_changes.items() if abs(v) > 5]
    return {
        "high_risk_positions": high_risk,
        "risk_summary": f"{len(high_risk)} positions moved significantly (>5%)."
    }
