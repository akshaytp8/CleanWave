import streamlit as st
import sys, os
_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _root not in sys.path:
    sys.path.insert(0, _root)
from data.real_data import get_all_wards_summary

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer { visibility: hidden; }
[data-testid="stHeaderActionElements"] { display: none !important; }
header { visibility: visible; }
.stApp { background: #0a0f0d; color: #e8ede9; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }
[data-testid="stSidebar"] { background: #0d1410 !important; border-right: 1px solid #1e2e24; }
.stButton > button { background: #166534 !important; color: #dcfce7 !important; border: none !important; border-radius: 8px !important; font-weight: 600 !important; padding: 0.6rem 1.5rem !important; font-size: 0.9rem !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:1.2rem 0;border-bottom:1px solid #1e2e24;margin-bottom:1rem;">
        <div style="font-size:1.5rem;font-weight:700;color:#e8ede9;">♻️ CleanWave</div>
        <div style="font-size:0.7rem;color:#4ade80;font-family:'DM Mono',monospace;margin-top:3px;">Tirurangadi Municipality · Kerala</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Main**")
    st.page_link("app.py", label="Live Overview", icon="📊")
    st.page_link("pages/0_home.py", label="About CleanWave", icon="ℹ️")
    st.page_link("pages/1_waste_map.py", label="Waste Map", icon="🗺️")
    st.markdown("**Intelligence**")
    st.page_link("pages/2_forecasting.py", label="Forecasting", icon="📈")
    st.page_link("pages/3_routes.py", label="Route Optimizer", icon="🛣️")
    st.page_link("pages/4_llm_chat.py", label="AI Assistant", icon="🤖")
    st.page_link("pages/6_cv_classify.py", label="Waste Classifier", icon="📷")
    st.page_link("pages/9_bin_monitor.py", label="Bin Monitor", icon="🎥")
    st.markdown("**People**")
    st.page_link("pages/5_citizens.py", label="Citizens & Rewards", icon="👥")
    st.markdown("**Operations**")
    st.page_link("pages/8_driver_view.py", label="Driver View", icon="🚛")

city = get_all_wards_summary()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="padding:3rem 0 2rem 0;border-bottom:1px solid #1e2e24;margin-bottom:2rem;">
    <div style="font-size:0.8rem;color:#4ade80;font-family:'DM Mono',monospace;
                letter-spacing:0.15em;text-transform:uppercase;margin-bottom:0.75rem;">
        India Innovates 2026 · Urban Solutions Track
    </div>
    <div style="font-size:3rem;font-weight:700;color:#e8ede9;line-height:1.1;margin-bottom:1rem;">
        CleanWave
    </div>
    <div style="font-size:1.2rem;color:#6b8f74;max-width:600px;line-height:1.6;margin-bottom:1.5rem;">
        AI-powered circular waste intelligence for Tirurangadi Municipality, Kerala.
        A prototype dashboard using simulated data; it is not connected to municipal IoT bins or truck tracking.
    </div>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;">
        <div style="background:#0d2010;border:1px solid #4ade8040;border-radius:8px;padding:0.5rem 1rem;font-size:0.82rem;color:#4ade80;">
            🟢 {city['daily_waste_monitored_tonnes']:,} tonnes/day sample scenario
        </div>
        <div style="background:#1a0800;border:1px solid #f8717140;border-radius:8px;padding:0.5rem 1rem;font-size:0.82rem;color:#f87171;">
            🔴 {city['daily_landfill_reduction']} t/day sample diversion scenario
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Problem ───────────────────────────────────────────────────────────────────
st.markdown("### The Problem")
col1, col2, col3 = st.columns(3)
problems = [
    ("Local data needed", "Waste generated", "Configure this pilot with verified local-body records", "#ef4444"),
    ("Local data needed", "Processing destinations", "Add approved collection and processing facilities", "#f59e0b"),
    ("Pilot scenario", "Collection operations", "Tune schedules and routes with local operators", "#60a5fa"),
]
for col, (stat, label, desc, color) in zip([col1, col2, col3], problems):
    with col:
        st.markdown(f"""
        <div style="background:#111a15;border:1px solid #1e2e24;border-radius:12px;padding:1.25rem;min-height:160px;box-sizing:border-box;overflow-wrap:break-word;">
            <div style="font-size:1.05rem;font-weight:700;line-height:1.3;color:{color};font-family:'DM Sans',sans-serif;word-break:normal;">{stat}</div>
            <div style="font-size:0.85rem;font-weight:600;color:#e8ede9;margin:0.4rem 0;">{label}</div>
            <div style="font-size:0.78rem;color:#6b8f74;line-height:1.55;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

# ── Solution ──────────────────────────────────────────────────────────────────
st.markdown("### How CleanWave Works")
steps = [
    ("📡", "Fill-Level Simulation", "Sample bin fill levels change in software. No Tirurangadi IoT bins are connected."),
    ("🤖", "AI Classification", "Upload an image or use a camera for a demo waste classification; results are not municipal inspection records."),
    ("📈", "Sample Forecasting", "Forecasts use generated history, not verified Tirurangadi collection measurements."),
    ("🚛", "Demo Route Optimisation", "Routes use illustrative collection points and simulated fill levels; they are not road-verified or dispatched to trucks."),
    ("🏆", "Citizen Incentives", "Sample points and rewards illustrate a possible system; confirm real participants, partners, and rules locally."),
    ("♻️", "Circular Economy", "Diversion and material-flow figures are illustrative scenarios, not measured waste or live tracking."),
]
col_a, col_b, col_c = st.columns(3)
for i, (icon, title, desc) in enumerate(steps):
    col = [col_a, col_b, col_c][i % 3]
    with col:
        st.markdown(f"""
        <div style="background:#111a15;border:1px solid #1e2e24;border-radius:12px;
                    padding:1.1rem;margin-bottom:0.75rem;">
            <div style="font-size:1.4rem;margin-bottom:0.4rem;">{icon}</div>
            <div style="font-size:0.88rem;font-weight:600;color:#e8ede9;margin-bottom:0.3rem;">{title}</div>
            <div style="font-size:0.75rem;color:#6b8f74;line-height:1.5;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

# ── Navigation guide ──────────────────────────────────────────────────────────
st.markdown("### Explore the Dashboard")
nav_items = [
    ("🏠", "Overview", "Dashboard metrics use simulated or configured sample data, not verified municipal reporting"),
    ("🗺️", "Waste Map", "Shows illustrative collection-point coordinates and simulated fill levels"),
    ("📈", "Forecasting", "Forecasts are based on generated sample history, not verified local measurements"),
    ("🚛", "Route Optimizer", "Demo routes use illustrative coordinates; they are not road-verified or dispatched"),
    ("🤖", "AI Assistant", "Ask about configured data; answers may reflect sample rather than verified local records"),
    ("👥", "Citizens & Rewards", "Sample leaderboard and rewards; citizen names and points are not verified"),
    ("📷", "Waste Classifier", "Classify an uploaded image or camera frame for demonstration"),
    ("♻️", "Circular Economy", "Illustrative material-flow scenario; configure verified local data before use"),
    ("🚛", "Driver View", "Displays optimizer-generated demo routes; it does not track trucks or dispatch jobs"),
    ("🎥", "Bin Monitor", "Analyze an uploaded sorting video; no live bin-monitoring devices are connected"),
]
col1, col2 = st.columns(2)
for i, (icon, title, desc) in enumerate(nav_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        st.markdown(f"""
        <div style="display:flex;gap:0.75rem;padding:0.6rem 0.75rem;background:#111a15;
                    border:1px solid #1e2e24;border-radius:8px;margin-bottom:0.4rem;">
            <div style="font-size:1.1rem;flex-shrink:0;">{icon}</div>
            <div>
                <div style="font-size:0.82rem;font-weight:600;color:#e8ede9;">{title}</div>
                <div style="font-size:0.72rem;color:#6b8f74;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

# ── Deployment model ──────────────────────────────────────────────────────────
st.markdown("### Deployment & Business Model")
col_d1, col_d2, col_d3 = st.columns(3)
with col_d1:
    st.markdown("""
    <div style="background:#111a15;border:1px solid #1e2e24;border-radius:12px;padding:1.25rem;">
        <div style="font-size:0.75rem;color:#4ade80;font-weight:700;text-transform:uppercase;
                    letter-spacing:0.08em;margin-bottom:0.75rem;">💰 Funding</div>
        <div style="font-size:0.8rem;color:#6b8f74;line-height:1.8;">
            <div>• Explore eligible state and national programs</div>
            <div>• Confirm grant eligibility with the local body</div>
            <div>• Local-body and community partnerships</div>
            <div>• Funding assumptions require local validation</div>
            <div style="margin-top:0.5rem;color:#e8ede9;font-weight:600;">Pilot budget: to be determined</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col_d2:
    st.markdown("""
    <div style="background:#111a15;border:1px solid #1e2e24;border-radius:12px;padding:1.25rem;">
        <div style="font-size:0.75rem;color:#60a5fa;font-weight:700;text-transform:uppercase;
                    letter-spacing:0.08em;margin-bottom:0.75rem;">🔧 Hardware</div>
        <div style="font-size:0.8rem;color:#6b8f74;line-height:1.8;">
            <div>• Sensor and camera requirements: to be assessed</div>
            <div>• Confirm collection points with local teams</div>
            <div>• Installation and connectivity: to be quoted</div>
            <div style="margin-top:0.5rem;color:#e8ede9;font-weight:600;">Hardware budget: to be determined</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col_d3:
    st.markdown("""
    <div style="background:#111a15;border:1px solid #1e2e24;border-radius:12px;padding:1.25rem;">
        <div style="font-size:0.75rem;color:#fbbf24;font-weight:700;text-transform:uppercase;
                    letter-spacing:0.08em;margin-bottom:0.75rem;">📊 ROI</div>
        <div style="font-size:0.8rem;color:#6b8f74;line-height:1.8;">
            <div>• Measure route distance against a local baseline</div>
            <div>• Track collection and processing costs</div>
            <div>• Quantify diversion with verified weights</div>
            <div>• Validate emissions assumptions locally</div>
            <div style="margin-top:0.5rem;color:#e8ede9;font-weight:600;">Pilot outcomes: not yet measured</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
