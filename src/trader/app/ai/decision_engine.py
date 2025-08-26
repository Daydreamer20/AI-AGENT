from typing import Literal

Signal = Literal["buy", "sell", "hold"]


def decide() -> Signal:
	return "hold"