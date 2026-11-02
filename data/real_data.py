"""Reference waste and population estimates used by the dashboard."""

from typing import Any

from data.synthetic_data import DELHI_WARDS

DELHI_TOTAL_WASTE_TPD = 10_500
DELHI_TOTAL_POPULATION = 16_787_941

BASELINE_LANDFILL_RATE = 0.77
BASELINE_RECYCLING_RATE = 0.15
BASELINE_COMPOST_RATE = 0.08

CYCLEIQ_LANDFILL_RATE = 0.50
CYCLEIQ_RECYCLING_RATE = 0.30
CYCLEIQ_COMPOST_RATE = 0.20

_WARD_COUNT = len(DELHI_WARDS)
_POPULATION_PER_WARD = DELHI_TOTAL_POPULATION // _WARD_COUNT
_WASTE_PER_WARD = DELHI_TOTAL_WASTE_TPD / _WARD_COUNT

WARD_REAL_DATA: dict[str, dict[str, Any]] = {
    ward["id"]: {
        "ward_id": ward["id"],
        "ward_name": ward["name"],
        "population": _POPULATION_PER_WARD,
        "daily_waste_tonnes": round(_WASTE_PER_WARD, 1),
    }
    for ward in DELHI_WARDS
}


def get_ward_waste_stats(ward_id: str) -> dict[str, Any] | None:
    """Return the reference waste estimate for a ward ID, if it is known."""
    return WARD_REAL_DATA.get(ward_id)


def get_all_wards_summary() -> dict[str, Any]:
    """Return the city-wide reference metrics shown on the dashboard."""
    daily_landfill_reduction = round(
        DELHI_TOTAL_WASTE_TPD
        * (BASELINE_LANDFILL_RATE - CYCLEIQ_LANDFILL_RATE)
    )
    current_daily_landfill = round(
        DELHI_TOTAL_WASTE_TPD * BASELINE_LANDFILL_RATE
    )
    daily_co2_saved_tonnes = round(daily_landfill_reduction * 0.9, 1)

    return {
        "daily_waste_monitored_tonnes": DELHI_TOTAL_WASTE_TPD,
        "total_population_covered": _POPULATION_PER_WARD * _WARD_COUNT,
        "coverage_pct": round(
            _POPULATION_PER_WARD * _WARD_COUNT / DELHI_TOTAL_POPULATION * 100,
            1,
        ),
        "daily_landfill_reduction": daily_landfill_reduction,
        "current_daily_landfill": current_daily_landfill,
        "daily_co2_saved_tonnes": daily_co2_saved_tonnes,
        "annual_co2_saved_tonnes": round(daily_co2_saved_tonnes * 365),
        "source": "CPCB Annual Report 2023; Census 2011; CycleIQ scenario estimates",
    }
