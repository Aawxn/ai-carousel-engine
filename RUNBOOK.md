# PRD 4: Creative AI Carousels — Operations Runbook

> **Audience:** Non-technical operators, content leads, and graphic designers.  
> **Rule:** Every failure posts to `#publishing-alerts` or `#ops-alerts` in plain English with this fix guide.

---

## Common Issues & Immediate Fixes

### 1. Slide Text Overflow Warning (`CopyFitError`)
* **What happened:** An AI-generated headline or body card exceeded the designer's character limit (e.g. body > 100 characters).
* **Fix:** The pre-render validator intercepts this automatically. In Notion, edit the slide text to be more concise (under character budget in `brand_tokens.json`) or set `dirty_slides: [N]` to re-trigger.

### 2. Designer Updates Fonts / Colors
* **What happened:** The graphic designer wants to update brand accent colors (e.g., from `#6366F1` to a festive shade) or font weights.
* **Fix:** Open `brand_tokens.json` in Notion or Git, update `"primary_accent"` or `"font_family"`, and save. **Zero Python code needs to be modified.**

### 3. Re-rendering a Single Slide (`dirty_slides`)
* **What happened:** Founder reviewed a carousel and noticed a typo on Slide 3.
* **Fix:** In Notion, edit Slide 3 text and flag `dirty_slides: [3]`. The engine preserves Slides 1, 2, 4, 5 from cache and regenerates only Slide 3 in <100ms.
