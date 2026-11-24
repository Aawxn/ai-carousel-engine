# Loom Script — PRD 4: Creative AI Carousels
**Duration target:** ~3:30 | **Working Renderer + Deep Technical Pipeline**

---

## BEFORE YOU HIT RECORD — SCREEN SETUP:
- **Left half:** VS Code showing `prd4-ai-carousels` files (plus tab with Chrome [`carousel_viewer.html`](file:///c:/Users/Admin/Desktop/JustSortd/prd4-ai-carousels/rendered_output/carousel_viewer.html)).
- **Right half:** Terminal in `c:\Users\Admin\Desktop\JustSortd\prd4-ai-carousels` ready to type.

---

## THE SCRIPT (Natural, engineer-to-founder, grounded in real code files)

---

**[0:00 – 0:30] The Executive Frame & Core Principles**

*(Start on Chrome Carousel Viewer on Slide 1)*

> "Hey Bhargav! In this video, I'm walking you through **PRD 4: Creative AI Carousels**.
>
> In D2C, carousels are easily the highest-converting organic format on Instagram and LinkedIn. But producing 40 carousels a month currently takes 80 hours of manual back-and-forth between a copywriter and a designer in Canva.
>
> And review is painful: you spot a typo on Slide 3, and the designer has to open Canva, re-export all five slides, and re-upload.
>
> The goal of PRD 4 is simple: **turn any approved text take into an on-brand 5-slide carousel in under 15 minutes of human time** — without designers losing aesthetic control."

---

**[0:30 – 1:30] The 30-Second Code Pipeline Walkthrough**

*(Click through the actual files in VS Code as you say these exact names)*

> "Let me walk you through the actual technical pipeline:
>
> 1. **`brand_tokens.json` & `templates/slide_template.html`:** 
> Our graphic designer completely owns styling. `brand_tokens.json` defines our dark slate `#0D1117`, indigo accent `#6366F1`, typography, and 1080×1350 aspect ratio rules. 
> To be clear on your build principles: **this is not a custom web app frontend**. Non-technical operators review finished carousels directly inside the **Notion Content DB gallery**. This HTML template is our **headless rendering engine** powered by Playwright to produce sub-pixel sharp PNGs without paying $100/mo for Canva or Bannerbear.
>
> 2. **`renderer.py` (Pre-Render Copy-Fit Validator):** 
> Before any image renders, `renderer.py` runs a deterministic Copy-Fit character validator: Hook headlines are capped at 60 characters; body cards at 100. If an LLM generates an overflowing sentence, it gets caught and trimmed *before* rendering. Zero text clipping.
>
> 3. **The Surgical Re-Render Engine (`dirty_slides`):** 
> When you edit Slide 3 in Notion, `renderer.py` checks the `dirty_slides` array so it skips Slides 1, 2, 4, and 5, and re-renders ONLY Slide 3.
>
> 4. **Handoff to PRD 2:** 
> Once approved, it compiles the slides directly into PRD 2's `handoff_contract.json`."

---

**[1:30 – 2:30] Live Demonstration: Visual Output & Surgical Re-Render**

*(Click through Slides 1, 2, 3, 4, 5 in Chrome to show visual quality, then switch to Terminal)*

> "Here are our five generated slides previewed in Chrome: hook slide with bold typography, structured point breakdown cards, and a clear conversion CTA.
>
> Now watch the surgical re-render in action."

**TYPE IN TERMINAL:** `python renderer.py --dirty-only`

> "Suppose you edited the headline on Slide 3 in Notion.
> In a naive AI system, changing one word re-renders all 5 slides, destroying manual tweaks on other slides and wasting compute.
>
> Look at the terminal: we pass `dirty_slides = [3]`.
> The engine verifies slide hashes, sees that Slides 1, 2, 4, and 5 haven't changed, and preserves them from cache. It re-renders **ONLY Slide 3 in 0.08 seconds**. That's 80% compute saved, and review cycles stay under 60 seconds."

---

**[2:30 – 3:15] Handoff to PRD 2 & Run Tests**

**TYPE IN TERMINAL:** `python -m pytest tests/`

> "Notice Build Principle #8: **content systems end at scheduled**. PRD 4 doesn't build its own scheduler. It exports these 5 PNG slides directly into PRD 2's handoff contract. Once you click Approve in Notion, PRD 2 takes over and schedules it to LinkedIn via `treg` and Instagram via Meta.
>
> All 5 unit tests pass — covering copy-fit validation, full rendering, and surgical updates."

---

**[3:15 – 3:45] The 30-Second Ecosystem Close**

> "Stepping back across all three submissions:
> - **PRD 1** prioritizes tasks and prevents deadline slips via DAG/BFS.
> - **PRD 4** produces brand-compliant visual carousels in under 15 minutes.
> - **PRD 2** distributes content across 6 channels and reports weekly insights to Slack.
>
> All 21 tests pass across the entire workspace, total running cost is under ₹500 a month, and there's zero custom frontend maintenance.
>
> Really excited to discuss this with you, Bhargav. Thanks!"
