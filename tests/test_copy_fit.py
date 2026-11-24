"""
tests/test_copy_fit.py - Verifies deterministic copy-fit character budgets.
"""

import pytest
from renderer import CopyFitValidator, CarouselRenderer


def test_copy_fit_valid_slide():
    validator = CopyFitValidator()
    slide = {
        "slide_index": 2,
        "slot_type": "POINT_BREAKDOWN",
        "headline": "Rule #1: Pre-book express air freight lanes",
        "body_copy": "Surface cargo gets jammed 10 days before Diwali. Secure guaranteed 48-hour air freight lanes for high-velocity SKUs."
    }
    errors = validator.validate_slide(slide)
    assert len(errors) == 0


def test_copy_fit_overflow_detected():
    validator = CopyFitValidator()
    overflow_slide = {
        "slide_index": 2,
        "slot_type": "POINT_BREAKDOWN",
        "headline": "This headline is intentionally written to be way too long and clearly exceed sixty characters limit",
        "body_copy": "Normal body copy."
    }
    errors = validator.validate_slide(overflow_slide)
    assert len(errors) > 0
    assert "Headline has" in errors[0]
    assert "exceeds max 60" in errors[0]
