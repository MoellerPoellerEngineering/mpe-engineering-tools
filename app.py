from pathlib import Path
import tomllib

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
LINKS_PATH = APP_DIR / "app_links.toml"

st.set_page_config(
    page_title="MPE Engineering Tools",
    page_icon=str(APP_DIR / "assets" / "mpe_app_icon.png"),
    layout="wide",
)

with LINKS_PATH.open("rb") as handle:
    app_links = tomllib.load(handle).get("apps", {})

st.image(str(APP_DIR / "assets" / "mpe_logo.png"), width=270)
st.title("MPE Engineering Tools")
st.write("Engineering analysis tools from Moeller & Poeller Engineering.")

tools = (
    (
        "⚡",
        "Load Flow Dashboard",
        "Explore PowerFactory load-flow sweeps, plots and equipment limit checks.",
        "Input: PowerFactory CSV results, optionally with a ZIP archive and mapping workbook.",
        app_links.get("load_flow", ""),
    ),
    (
        "📈",
        "Frequency Sweep Analyser",
        "Compare frequency-dependent resistance, reactance and impedance curves.",
        "Input: Excel frequency-sweep workbook with R1 and X1 sheets; R0 and X0 are optional.",
        app_links.get("frequency_sweep", ""),
    ),
    (
        "〰️",
        "Harmonic Analysis Dashboard",
        "Review harmonic results and total harmonic distortion against selected limits.",
        "Input: Excel results, optionally with Cases_description and Limits workbooks or a ZIP bundle.",
        app_links.get("harmonics", ""),
    ),
)

columns = st.columns(3, gap="large")
for column, (icon, name, description, expected_input, url) in zip(columns, tools):
    with column.container(border=True):
        st.markdown(f"### {icon} {name}")
        st.write(description)
        st.caption(expected_input)
        if url:
            st.link_button("Open application", url, width="stretch")
        else:
            st.caption("Deployment URL will be added after the dashboard is deployed.")

st.info(
    "These tools require the specified input formats. A competent engineer must review "
    "the results before they are used in engineering decisions."
)