def position_size(balance: float, risk_pct: float, stop_distance: float) -> float:
	if balance <= 0 or risk_pct <= 0 or stop_distance <= 0:
		raise ValueError("Inputs must be positive")
	risk_amount = balance * risk_pct
	return risk_amount / stop_distance