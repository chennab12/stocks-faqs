# Stocks & Investing Compass

Standalone replacement for the nutrition app's content and tab structure. All tabs concern stocks and investing: 16 progressive lessons, a master cheatsheet, overview, 7 calculator modes, investing-style comparison, research/SMART-goal worksheet and official sources. Tables include examples, investor takeaways and formulas. Each lesson has a knowledge check and a code-native animated memory cue that supports reduced-motion settings.

## Run

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud

Upload `app.py`, `content.py`, `calculations.py` and `requirements.txt` to your repository, keeping them in the same folder. Set the main file to `app.py` (or its repository-relative path). This package does not modify the existing live deployment.

## Assumptions

US educational context, sources reviewed October 1, 2026. No live market data, trade execution, brokerage login, stock picks or guaranteed returns. Examples are hypothetical. Contributions occur at month-end; return scenarios use effective monthly compounding; annual fees are modeled multiplicatively; inflation discounts final dollars. Research notes can be downloaded but are not persisted across sessions. Consult current IRS guidance for tax rules; no annual thresholds or personalized tax calculations are embedded.
