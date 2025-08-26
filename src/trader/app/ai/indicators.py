from typing import List


def simple_moving_average(values: List[float], window: int) -> float:
	if not values or window <= 0 or len(values) < window:
		raise ValueError("Insufficient values or invalid window")
	return sum(values[-window:]) / window