"""
tests/test_surgical_render.py - Verifies surgical partial re-render and compute savings.
"""

import json
from pathlib import Path
import pytest
from renderer import CarouselRenderer


@pytest.fixture
def sample_carousel_data():
    path = Path(__file__).resolve().parent.parent / "carousel_contract.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_full_carousel_render(sample_carousel_data):
    renderer = CarouselRenderer()
    res = renderer.execute_render(sample_carousel_data, force_all=True)

    assert res["render_mode"] == "FULL_RENDER"
    assert res["total_slides"] == 5
    assert res["slides_re_rendered"] == 5
    assert res["slides_cached"] == 0
    assert res["compute_saved_pct"] == 0.0


def test_surgical_single_slide_render(sample_carousel_data):
    renderer = CarouselRenderer()
    # Edit Slide 3 ONLY
    sample_carousel_data["dirty_slides"] = [3]

    res = renderer.execute_render(sample_carousel_data, force_all=False)

    assert res["render_mode"] == "SURGICAL_PARTIAL_RENDER"
    assert res["slides_re_rendered"] == 1
    assert res["slides_cached"] == 4
    assert res["compute_saved_pct"] == 80.0

    slide_3 = [s for s in res["rendered_slides"] if s["slide_index"] == 3][0]
    slide_1 = [s for s in res["rendered_slides"] if s["slide_index"] == 1][0]

    assert slide_3["status"] == "RE_RENDERED"
    assert slide_1["status"] == "PRESERVED_CACHED"
