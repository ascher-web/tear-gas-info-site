# Beyond the Burning: The Human Health Effects of Tear Gas


## Pages
| # | Route | Template | What it shows |
|---|---|---|---|
| 1 | `/` | `home.html` | Homepage, topic cards, evidence legend, survey call-out |
| 2–7 | `/topic/<slug>` | `topic.html` | Understanding Tear Gas, Respiratory, Reproductive, Long-Term, Vulnerable Populations, Medical Care |
| 8 | `/research` | `research.html` | Research library with every cited study |
| – | `/minneapolis` | `minneapolis.html` | Minneapolis community health survey |
| – | `/report` (GET) | `reportForm.html` | Exposure report form |
| – | `/report` (POST) | `reportSuccess.html` | Shows the submitted report + matching research |

Page text and sources live in `content.py`.

## Assignment checklist
- **Flask site runs:** `flask run`
- **One distinct page:** 10 pages total
- **Template inheritance:** every page uses `{% extends "base.html" %}` with `title` and `content` blocks
- **Functional form:** `reportForm.html` posts to `/report`, validates required fields, shows an error message,
  and displays the data on `reportSuccess.html`
- **Bonus:** submitted via GitHub

## How to run
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run
```
Then open http://127.0.0.1:5000

## Sources
See the Research Library page. Main sources: CDC Riot Control Agents fact sheet; Hassan et al. 2023
(Frontiers in Epidemiology); Torgrimson-Ojerio et al. 2021 (BMC Public Health); Arbak et al. 2014
(Scientific World Journal); Dimitroglou et al. 2015 (IJERPH); Rothenberg et al. 2016 (Ann NY Acad Sci);
Haar et al. 2017 (BMC Public Health); Brown et al. 2021 (Inhalation Toxicology).

*For educational purposes only. Not medical advice.*
