from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def test_landing_page_shows_three_tools_and_unconfigured_link_placeholders():
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
    assert visible_text.count("Deployment URL will be added") == 3