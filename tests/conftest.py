"""
conftest.py - Pytest path configuration for PRD 4.
"""
import sys
from pathlib import Path

prd4_root = Path(__file__).resolve().parent.parent
if str(prd4_root) not in sys.path:
    sys.path.insert(0, str(prd4_root))
