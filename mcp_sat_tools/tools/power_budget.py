from typing import TypedDict


class PowerBudgetResult(TypedDict):
    required_bol_array_power_w: float
    required_eol_array_power_w: float
    battery_capacity_wh: float
    notes: str


def compute_power_budget_core(
    payload_power_w: float,
    eclipse_fraction: float,
    bus_power_margin: float,
) -> PowerBudgetResult:
    """
    Stub power-budget calculation.

    Replace this with your real logic or call into your existing backend.
    For now it just does simple placeholder math so we can wire up MCP.
    """

    # Extremely simplified placeholder logic:
    # BOL array power = payload power * (1 + margin)
    bol_array_power = payload_power_w * (1.0 + bus_power_margin)

    # EOL array power = BOL * 0.8 (fake degradation factor)
    eol_array_power = bol_array_power * 0.8

    # Battery capacity = payload power * eclipse_fraction * 1.5 (totally fake)
    battery_capacity_wh = payload_power_w * eclipse_fraction * 1.5

    return {
        "required_bol_array_power_w": bol_array_power,
        "required_eol_array_power_w": eol_array_power,
        "battery_capacity_wh": battery_capacity_wh,
        "notes": "Stub calculation. Replace with real power budget logic.",
    }
