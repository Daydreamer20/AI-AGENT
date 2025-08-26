from dataclasses import dataclass
from typing import Any


@dataclass
class MCPClient:
	base_url: str

	async def ping(self) -> dict[str, Any]:
		return {"ok": True, "base_url": self.base_url}