# CleanWave — AI-Powered Circular Waste Intelligence for Tirurangadi

## Pilot Scope

CleanWave is a software prototype scoped to a possible **Tirurangadi Municipality pilot** in Malappuram district, Kerala. The ward labels come from the 39-ward list on the [Government of Kerala Local Self Government Department's 2020 election roster](https://lsgkerala.gov.in/en/lbelection/electdmemberdet/2020/1274); that historical list does not verify today's ward count, names, or boundaries. The repository's waste estimates, population coverage, collection schedules, and processing destinations are demonstration data. Plotted coordinates are approximate markers around Chemmad, not ward boundaries, centroids, or surveyed collection points.

The pilot should establish its baseline with local operators before treating any dashboard metric as a measured result.

---

## What CleanWave Does

CleanWave is a prototype dashboard demonstrating possible waste-management workflows using computer vision, simulated fill levels, route optimization, and forecasting. It is not currently connected to Tirurangadi's municipal bins, citizen registry, or truck fleet.

The system targets **community collection points** where residents hand over segregated waste to local collection teams. Collection workflows, accepted material categories, service schedules, and disposal destinations must follow the participating local body's procedures.

---

## How It Works — The Full Story

### 1. Computer Vision at Source
A camera mounted above a community collection point can help monitor waste sorting. The local body should determine the appropriate categories, bin colors, signage, and handling procedures for the pilot.

The classifier uses the general-purpose **YOLOv8n** object-detection model and maps a limited set of detected object labels to broad waste categories:
- **Biodegradable** — food waste, organic matter
- **Recyclable** — plastic, paper, metal, glass
- **Hazardous/e-waste** — a limited set of supported electronic-device labels

A **demo segregation score** (0–100) is calculated from the generated category percentages. This is not a validated waste audit: the model was not trained specifically for local waste, and the fallback may estimate categories from image colour or generate sample values.

### 2. Citizen Incentives Tied to Segregation Quality
The prototype can award sample points when a classification score reaches its configured threshold. It currently awards points to up to five records in that ward; it does not verify participation or identify the person who sorted the waste. Seeded citizen names and point totals are generated demo data, not verified residents or activity records.

Any citizen reward program is illustrative until participants, local partners, redemption processes, and approvals are verified.

### 3. IoT Fill Level Monitoring
In a deployed system, an **ultrasonic sensor** could measure the distance to the waste surface and send fill readings to an API. This prototype has no connected Tirurangadi bin sensors and receives no GSM or LoRa feed.

> The API seeds illustrative collection points with approximate coordinates around Chemmad. It randomizes their fill levels when it starts, then a background simulation updates about 20% of points every 30 seconds. This is simulated data, not a sensor feed or a verified map of bins.

### 4. AI-Optimised Route Planning
CleanWave uses **Google OR-Tools** with a GlobalSpanCostCoefficient constraint to create balanced demo routes from stored fill levels and illustrative coordinates. The optimizer estimates distances between points; the map draws straight lines between stops. It does not calculate road directions, dispatch trucks, or track vehicles.

The route page displays estimated distance, time, emissions, and stop counts. These are prototype estimates, not measured savings or operational dispatch data.

### 5. 7-Day Waste Volume Forecasting
Using **Facebook Prophet** (with a statistical fallback for environments where Prophet is unavailable), CleanWave generates seven-day forecasts from the stored history. On an empty database, that history is synthetically generated; forecasts are not verified Tirurangadi measurements.

These forecasts are for demonstration and should not be used to schedule staff or vehicles without validated local data.

### 6. Circular Economy Tracking
The dashboard includes an illustrative scenario for waste diversion and environmental impact:
- **Recycling and composting rates** — fixed scenario assumptions, not measured recovery
- **CO₂ savings** — scenario estimates against a landfill baseline, not measured emissions
- **Material flow Sankey diagram** — visualises the illustrative scenario, not tracked waste

### 7. AI Chat for City Officials
A natural language interface powered by **Groq / GPT-OSS 20B** can answer questions using values passed from the database. When the database contains seeded demo records, answers reflect those records—not live or verified municipal data. A Groq API key and a model available to that key are required.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI + PostgreSQL (Neon) |
| ORM | SQLAlchemy |
| Computer Vision | YOLOv8n (Ultralytics) |
| Forecasting | Facebook Prophet + statistical fallback |
| Route Optimization | Google OR-Tools |
| LLM | Groq API / GPT-OSS 20B |
| Frontend | Streamlit |
| Maps | Folium + streamlit-folium |
| Charts | Plotly |
| Camera Input | streamlit-webrtc + aiortc |

---

## Project Structure

```
CleanWave/
├── main.py                          # FastAPI app + IoT simulation loop
├── database.py                      # Neon PostgreSQL connection
├── .env                             # Credentials (not committed)
├── requirements.txt
├── models/
│   ├── waste_model.py               # CollectionPoint, WasteClassification
│   ├── forecast_model.py            # WasteForecast, WasteHistory
│   └── citizen_model.py             # Citizen, CitizenActivity, OptimizedRoute
├── routers/
│   ├── waste_router.py              # CV classify, collection points, ward summary
│   ├── forecast_router.py           # 7-day forecasts, history
│   ├── routes_router.py             # OR-Tools route optimization
│   ├── dashboard_router.py          # KPIs + LLM query
│   └── citizens_router.py           # Leaderboard, register, activity
├── ml/
│   ├── cv_module.py                 # YOLOv8 + image-aware fallback
│   ├── forecasting.py               # Prophet + statistical fallback
│   ├── route_optimizer.py           # OR-Tools balanced routing
│   └── llm_engine.py                # Groq/GPT-OSS with database context
├── data/
│   ├── real_data.py                 # Fixed illustrative pilot-area scenario
│   └── synthetic_data.py            # 2020 ward roster and generated demo data
└── streamlit_app/
    ├── app.py                       # Overview dashboard
    └── pages/
        ├── 0_home.py                # About CleanWave
        ├── 1_waste_map.py           # Folium map + ward composition
        ├── 2_forecasting.py         # Prophet 7-day forecast per ward
        ├── 3_routes.py              # OR-Tools map + truck cards
        ├── 4_llm_chat.py            # AI chat using configured database context
        ├── 5_citizens.py            # Demo leaderboard, registration, and rewards
        ├── 6_cv_classify.py         # Camera or image classification demo
        ├── 8_driver_view.py         # Optimizer-generated route display
        └── 9_bin_monitor.py         # Uploaded-video sorting analysis
```

The Circular Economy view is a tab in the Overview dashboard, not a separate page.

---

## Setup & Running

### Prerequisites
- Python 3.11 (the version specified by `runtime.txt`)
- A Neon PostgreSQL database
- A Groq API key (for AI chat)

### Installation

```bash
git clone https://github.com/akshaytp8/CleanWave.git
cd CleanWave

python -m venv .venv
```

Activate the virtual environment, then install both the API and Streamlit dependencies. On Windows PowerShell, run `.venv\Scripts\Activate.ps1`; on macOS/Linux, run `source .venv/bin/activate`.

```bash
pip install -r requirements.txt -r streamlit_app/requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URL=your_neon_postgresql_connection_string
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

The Streamlit app checks `http://localhost:8000` first, then falls back to the configured hosted API URL. Set `API_URL` to your backend base URL (without `/api`) when using a different deployment. Configure it in the Streamlit process environment or Streamlit secrets; the frontend does not load `API_URL` from the root `.env` file.

### Running

**Terminal 1 — API:**
```bash
uvicorn main:app --reload --port 8000
```

**Terminal 2 — Streamlit:**
```bash
cd streamlit_app
streamlit run app.py
```

At startup, empty tables are seeded with synthetic/demo records: collection points (three per ward), 150 citizens, 180 days of waste history, and initial waste classifications. The ward names follow the 2020 election roster; verify the current count, names, and boundaries with the municipality. Coordinates are approximate markers, not surveyed collection points. The fixed waste scenario is not live data or verified population coverage.

Existing records in non-empty tables are generally not re-seeded. **Exception:** each API startup assigns new random fill levels to every existing collection point, and the simulation then changes some levels every 30 seconds. Back up any database you care about and do not treat these values as sensor readings.

- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Dashboard: http://localhost:8501

---

## Pages

| Page | Purpose |
|---|---|
| Overview | Dashboard KPIs, simulated fill-level charts, seeded citizen statistics, illustrative waste scenario |
| About CleanWave | Prototype description, sample-data caveats, and navigation guide |
| Waste Map | Collection-point markers at approximate coordinates with simulated fill levels and seeded composition |
| Forecasting | Seven-day forecast and history based on generated sample data unless replaced |
| Route Optimizer | Balanced routes and straight-line map display from stored coordinates; no truck dispatch |
| AI Chat | Natural-language queries using database values via Groq/GPT-OSS 20B |
| Citizens & Rewards | Leaderboard, tiers, registration, rewards, and ward report cards; seeded citizens are fictional |
| Waste Classifier | Camera or image classification demo; YOLO labels and fallback estimates are not validated waste audits |
| Driver View | Displays optimizer-generated routes; does not track trucks |
| Bin Monitor | Uploaded-video sorting analysis; not a live connected bin-monitoring system |
| Circular Economy tab | Illustrative material-flow and diversion scenario in the Overview |

---

## Deployment Notes

The FastAPI backend runs locally and connects to the PostgreSQL database configured by `DATABASE_URL` (the project uses Neon). The Streamlit frontend can be deployed to Streamlit Cloud (share.streamlit.io) pointing to `streamlit_app/app.py`; configure `API_URL` in the Streamlit app settings to point to a publicly deployed API. The API must also be deployed for a hosted frontend to reach it.

For local demo (recommended for presentations), run both terminals and open `localhost:8501`.

---

