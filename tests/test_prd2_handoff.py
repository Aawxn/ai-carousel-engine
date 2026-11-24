"""
tests/test_prd2_handoff.py - Verifies that PRD 4 exports payloads compliant with PRD 2.
"""

import json
from pathlib import Path
from renderer import CarouselRenderer


def test_export_prd2_handoff_contract_structure():
    path = Path(__file__).resolve().parent.parent / "carousel_contract.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    renderer = CarouselRenderer()
    handoff = renderer.export_prd2_handoff(data)

    assert handoff["origin_prd"] == "PRD_4_AI_CAROUSELS"
    assert "target_channels" in handoff
    assert "media_assets" in handoff
    assert handoff["media_assets"][0]["media_type"] == "carousel_pdf"
    assert handoff["media_assets"][0]["aspect_ratio"] == "4:5"
    assert len(handoff["media_assets"][0]["slide_urls"]) == 5
    assert handoff["publish_status"] == "Pending Approval"
