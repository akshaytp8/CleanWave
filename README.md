# CycleIQ — AI-Powered Circular Waste Intelligence for Tirurangadi

> **India Innovates 2026 Hackathon** · Team Sigmoid · JSS University  
> Domain: Urban Solutions · Prize Pool: ₹10,00,000+

---

## The Problem

CycleIQ is being adapted as a **Tirurangadi Municipality pilot** in Malappuram district, Kerala. It uses the 39 ward names listed in the [Government of Kerala Local Self Government Department's 2020 election roster](https://lsgkerala.gov.in/en/lbelection/electdmemberdet/2020/1274). Verify the current ward list with the municipality before operational use. The repository's waste estimates, population coverage, collection schedules, and processing destinations remain demonstration data; the plotted ward coordinates are approximate markers around Chemmad, not ward boundaries or centroids.

The pilot should establish its baseline with local operators before treating any dashboard metric as a measured result.

---

## What CycleIQ Does

CycleIQ is an end-to-end waste intelligence platform that closes the loop between **citizens, bins, trucks, and city planners** using computer vision, IoT simulation, route optimization, and AI forecasting.

The system targets **community collection points** where residents hand over segregated waste to local collection teams. Collection workflows, accepted material categories, service schedules, and disposal destinations must follow the participating local body's procedures.

---

## How It Works — The Full Story

### 1. Computer Vision at Source
A camera mounted above a community collection point can help monitor waste sorting. The local body should determine the appropriate categories, bin colors, signage, and handling procedures for the pilot.

CycleIQ uses **YOLOv8**, a state-of-the-art real-time object detection model, to classify waste as:
- **Biodegradable** — food waste, organic matter
- **Recyclable** — plastic, paper, metal, glass
- **Hazardous** — electronics, batteries, chemicals

A **segregation score** (0–100) is calculated per classification based on how cleanly a single waste type dominates. High scores mean good segregation. Low scores trigger alerts.

### 2. Citizen Incentives Tied to Segregation Quality
When a ward's collection points consistently show high segregation scores, citizens in that ward earn points on the CycleIQ platform. This is community-level gamification — not individual surveillance — creating peer pressure and collective accountability. Citizens can view their ward's leaderboard and track their own contribution.

Any citizen reward program is a demonstration only until its local partners, redemption process, and approval are confirmed.

### 3. IoT Fill Level Monitoring
Each bin is equipped with an **ultrasonic sensor** that measures the distance from the sensor to the waste surface, calculating fill percentage. This data is transmitted in real time to the CycleIQ API via GSM or LoRa network.

> In the current prototype, fill levels are simulated via a background IoT loop that updates 20% of collection points every 30 seconds — demonstrating the real-time data pipeline. In production, this feed is replaced by actual sensor hardware. Sensor-based smart bins are already deployed commercially in Indian cities including Pune and Indore, as well as internationally by companies like Bigbelly and Sensoneo.

### 4. AI-Optimised Route Planning
CycleIQ uses **Google OR-Tools** with a GlobalSpanCostCoefficient constraint to generate balanced truck routes based on live fill data. Trucks are only dispatched to bins that are above a fill threshold, and routes are distributed evenly across the truck fleet to prevent any single truck being overloaded.

This replaces fixed-schedule collection — a major source of inefficiency — with demand-driven collection. The system visualises routes on an interactive map with per-truck details including estimated distance and number of stops.

### 5. 7-Day Waste Volume Forecasting
Using **Facebook Prophet** (with a statistical fallback for environments where Prophet is unavailable), CycleIQ can forecast waste volume for configured pilot wards. The current sample history is illustrative; replace it with verified Tirurangadi collection records.

This allows city planners to pre-position trucks and staff before high-volume periods (festivals, weekends, seasonal spikes) rather than reacting after bins overflow.

### 6. Circular Economy Tracking
CycleIQ quantifies the environmental impact of the system in real time:
- **Recycling diversion rate** — what percentage of waste is being recovered instead of landfilled
- **Composting potential** — organic waste available for composting
- **CO₂ savings** — calculated against a full-landfill baseline
- **Material flow Sankey diagram** — visualises where each tonne of waste goes

### 7. AI Chat for City Officials
A natural language interface powered by **Groq / Llama 3.1** allows city officials to query the system in plain English: *"Which ward has the highest hazardous waste concentration?"* or *"Which bins need urgent collection today?"* The LLM responds using real data from the database, not generic answers.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI + PostgreSQL (Neon) |
| ORM | SQLAlchemy |
| Computer Vision | YOLOv8n (Ultralytics) |
| Forecasting | Facebook Prophet + statistical fallback |
| Route Optimization | Google OR-Tools |
| LLM | Groq API / Llama 3.1 8B Instant |
| Frontend | Streamlit |
| Maps | Folium + streamlit-folium |
| Charts | Plotly |
| Live Camera | streamlit-webrtc + aiortc |

---

## Project Structure

```
cycleiq/
├── main.py                          # FastAPI app + IoT simulation loop
├── database.py                      # Neon PostgreSQL connection
├── .env                             # Credentials (not committed)
├── .env.example                     # Template for setup
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
│   └── llm_engine.py                # Groq/Llama with real DB context
├── data/
│   └── synthetic_data.py            # 39 Tirurangadi wards (2020 roster) and demo data
└── streamlit_app/
    ├── app.py                       # Main dashboard — 6 KPIs, alerts
    └── pages/
        ├── 1_waste_map.py           # Folium map + ward composition
        ├── 2_forecasting.py         # Prophet 7-day forecast per ward
        ├── 3_routes.py              # OR-Tools map + truck cards
        ├── 4_llm_chat.py            # AI chat with real data context
        ├── 5_citizens.py            # Leaderboard + register
        ├── 6_cv_classify.py         # Live camera + image upload classifier
        └── 7_circular_economy.py    # Sankey + CO₂ impact + diversion rates
```

---

## Setup & Running

### Prerequisites
- Python 3.10+
- A Neon PostgreSQL database
- A Groq API key

### Installation

```bash
git clone https://github.com/RAK2315/CycleIQ-Waste-Intelligence-System.git
cd CycleIQ-Waste-Intelligence-System

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic groq python-multipart
pip install streamlit plotly pandas numpy pillow httpx requests
pip install folium streamlit-folium
pip install ultralytics
pip install ortools
pip install streamlit-webrtc aiortc opencv-python-headless
```

### Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URL=your_neon_postgresql_connection_string
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

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

An empty database seeds automatically on first startup with synthetic pilot data for 39 wards, 150 citizens, and 180 days of waste history. The ward names follow the 2020 election roster; verify any subsequent delimitation or renaming with the municipality. Coordinates are illustrative markers, and summary metrics are not live measurements or verified population coverage. Existing database records are not automatically replaced or migrated.

- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Dashboard: http://localhost:8501

---

## Pages

| Page | Purpose |
|---|---|
| Overview | 6 live KPIs, fill level alerts, recent activity |
| Waste Map | Interactive Folium map of all collection points colour-coded by fill level, ward composition chart |
| Forecasting | 7-day Prophet forecast per ward, historical trend, all-wards comparison |
| Route Optimizer | OR-Tools balanced truck routes on map, per-truck stats, estimated savings |
| AI Chat | Natural language queries against live database via Groq/Llama 3.1 |
| Citizen Portal | Leaderboard, tier system (Bronze → Platinum), register new citizens |
| CV Classifier | Live webcam stream with YOLOv8 bounding boxes, or image upload mode |
| Circular Economy | Material flow Sankey, ward diversion rates, 30-day CO₂ savings trend |

---

## Deployment Notes

The FastAPI backend runs locally and connects to a hosted Neon PostgreSQL database. The Streamlit frontend can be deployed to Streamlit Cloud (share.streamlit.io) pointing to `streamlit_app/app.py`. For the full system to work when hosted, the API also needs to be deployed publicly — Railway.app or Render.com work well for this.

For local demo (recommended for presentations), run both terminals and open `localhost:8501`.

---

## Team

**Team Sigmoid — JSS University**
- Rehaan Ahmad Khan
- Krishna Agarwaal  
- Daksh Kumar

**Event:** India Innovates 2026 — World's Largest Civic Tech Hackathon  
**Pilot area:** Tirurangadi Municipality, Malappuram district, Kerala