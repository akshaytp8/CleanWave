"""Illustrative pilot scenario values shown by the dashboard."""

from typing import Any

from data.synthetic_data import TIRURANGADI_WARDS

PILOT_AREA_NAME = "Tirurangadi Municipality"
PILOT_SCENARIO_WASTE_TPD = 100

BASELINE_LANDFILL_RATE = 0.77
BASELINE_RECYCLING_RATE = 0.15
BASELINE_COMPOST_RATE = 0.08

CYCLEIQ_LANDFILL_RATE = 0.50
CYCLEIQ_RECYCLING_RATE = 0.30
CYCLEIQ_COMPOST_RATE = 0.20

_WARD_COUNT = len(TIRURANGADI_WARDS)
_WASTE_PER_WARD = PILOT_SCENARIO_WASTE_TPD / _WARD_COUNT

PILOT_WARD_DATA: dict[str, dict[str, Any]] = {
    ward["id"]: {
        "ward_id": ward["id"],
        "ward_name": ward["name"],
        "population": None,
        "daily_waste_tonnes": round(_WASTE_PER_WARD, 1),
    }
    for ward in TIRURANGADI_WARDS
}


def get_ward_waste_stats(ward_id: str) -> dict[str, Any] | None:
    """Return the reference waste estimate for a ward ID, if it is known."""
    return PILOT_WARD_DATA.get(ward_id)


def get_all_wards_summary() -> dict[str, Any]:
    """Return illustrative pilot-area metrics shown on the dashboard."""
    daily_landfill_reduction = round(
        PILOT_SCENARIO_WASTE_TPD
        * (BASELINE_LANDFILL_RATE - CYCLEIQ_LANDFILL_RATE)
    )
    current_daily_landfill = round(
        PILOT_SCENARIO_WASTE_TPD * BASELINE_LANDFILL_RATE
    )
    daily_co2_saved_tonnes = round(daily_landfill_reduction * 0.9, 1)

    return {
        "daily_waste_monitored_tonnes": PILOT_SCENARIO_WASTE_TPD,
        "total_population_covered": None,
        "coverage_pct": None,
        "daily_landfill_reduction": daily_landfill_reduction,
        "current_daily_landfill": current_daily_landfill,
        "daily_co2_saved_tonnes": daily_co2_saved_tonnes,
        "annual_co2_saved_tonnes": round(daily_co2_saved_tonnes * 365),
        "source": (
            f"Illustrative {PILOT_AREA_NAME} scenario only; replace with verified "
            "local-body waste, population, and processing data."
        ),
    }
