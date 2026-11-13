from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def test_landing_page_shows_three_tools_with_deployed_links():
    app = AppTest.from_file(str(APP_PATH), default_timeout=30).run()

    assert not app.exception
    assert app.title[0].value == "MPE Engineering Tools"
    visible_text = " ".join(
        [element.value for element in app.markdown]
        + [element.value for element in app.caption]
        + [element.value for element in app.info]
    )
    assert "Load Flow Dashboard" in visible_text
    assert "Frequency Sweep Analyser" in visible_text
    assert "Harmonic Analysis Dashboard" in visible_text
    assert sum("**Input:**" in element.value for element in app.markdown) == 3
    buttons = app.get("link_button")
    assert [button.url for button in buttons] == [
        "https://mpe-load-flow.streamlit.app/",
        "https://mpe-frequency-sweep.streamlit.app/",
        "https://mpe-harmonics.streamlit.app/",
    ]
