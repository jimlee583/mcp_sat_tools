from mcp.server.fastmcp import FastMCP

from .tools.demo_add import add_core
from .tools.power_budget import compute_power_budget_core, PowerBudgetResult

# Create the MCP server
mcp = FastMCP("SatelliteTools", json_response=True)


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Simple smoke-test tool to verify the MCP server wiring.
    """
    return add_core(a, b)


@mcp.tool()
def compute_power_budget(
    payload_power_w: float,
    eclipse_fraction: float,
    bus_power_margin: float,
) -> PowerBudgetResult:
    """
    Compute a (stub) GEO satellite power budget.

    Args:
        payload_power_w: Payload power in watts.
        eclipse_fraction: Fraction of the orbit in eclipse (0.0–1.0).
        bus_power_margin: Fractional power margin (e.g. 0.3 for 30%).

    Returns:
        PowerBudgetResult dict with BOL/EOL array power and battery capacity.
    """
    return compute_power_budget_core(
        payload_power_w=payload_power_w,
        eclipse_fraction=eclipse_fraction,
        bus_power_margin=bus_power_margin,
    )


if __name__ == "__main__":
    # Expose MCP over HTTP at http://localhost:8000/mcp
    mcp.run(transport="streamable-http")
