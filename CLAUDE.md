# Cataract - Claude Code Instructies

## Project
Wetenschappelijk informatieplatform over aangeboren staar (congenitaal cataract).

- **Locatie**: `E:\scripts\webscraper\CBSbuurt\cataract\`
- **URL**: `http://localhost:8093`
- **GitHub**: AnneVersion/cataract
- **GitHub Pages**: anneversion.github.io/cataract

## Startup Checklist
1. Start de server:
   ```bash
   python serve.py  # http://localhost:8093
   ```
2. Controleer:
   - [ ] Server start zonder errors op port 8093
   - [ ] `http://localhost:8093/` laadt index.html
   - [ ] Alle 6 pagina's laden zonder console errors
   - [ ] Navigatie werkt op alle pagina's
   - [ ] DC logo (dc-logo.svg) zichtbaar in navigatie
   - [ ] Persoonlijk dashboard toont checklist items
   - [ ] SVG illustraties (anterieure vs posterieure IOL) renderen correct

## Branch-strategie
- **main** = stabiel/productie
- **develop** = dagelijkse ontwikkeling (standaard werkbranch)
- **feature/*** = nieuwe features, maak aan vanuit develop

Werk op `develop`. Alleen mergen naar `main` als het stabiel is.

## Pagina's
| Pagina | URL | Beschrijving |
|--------|-----|-------------|
| `index.html` | `/` | Overzicht + persoonlijk dashboard |
| `behandelingen.html` | `/behandelingen.html` | Behandelingen en operaties |
| `onderzoek.html` | `/onderzoek.html` | Wetenschappelijk onderzoek |
| `voeding.html` | `/voeding.html` | Voeding en ooggezondheid |
| `klinieken.html` | `/klinieken.html` | Klinieken en specialisten |
| `bronnen.html` | `/bronnen.html` | Bronnen en referenties |

## Design
- **Thema**: Licht medisch (wit/blauw)
- **Fonts**: Merriweather (serif) + Inter (sans-serif)
- **Naam**: "Cataract" (normaal geschreven, NIET catARACT)
- **DC logo**: in navigatie (`dc-logo.svg`)
- **Components**: Evidence badges, alert boxes, citaat-referenties, timeline component
- **SVG illustraties**: anterieure vs posterieure IOL

## Persoonlijk Dashboard
Het dashboard is gebouwd rond de dochter van de eigenaar:
- **Geboortedatum**: 12-04-2004
- **Diagnose**: bilateraal congenitaal cataract
- **Operaties**: 2x geopereerd als baby
- **IOL's**: 1 anterieure IOL + 1 posterieure IOL
- **Ziekenhuis**: Het Oogziekenhuis Rotterdam (KinderOOGcentrum)

### Checklist items
Controles voor dochter: endotheelcellen, glaucoom, refractie, netvlies, nastaar, UV-bescherming.

## Bestanden
| Bestand | Functie |
|---------|---------|
| `index.html` | Overzicht + persoonlijk dashboard |
| `behandelingen.html` | Behandelingsmethoden |
| `onderzoek.html` | Wetenschappelijk onderzoek |
| `voeding.html` | Voeding en oogverzorging |
| `klinieken.html` | Klinieken en specialisten |
| `bronnen.html` | Referenties en bronmateriaal |
| `style.css` | Gedeelde styling |
| `dc-logo.svg` | Data Consultants logo in navigatie |
| `serve.py` | HTTP server op port 8093 |

## TODO
- [ ] Meer illustraties: oog anatomie, cataract proces, operatie stappen
- [ ] Perceptual learning pagina toevoegen (visuele training voor volwassenen)
- [ ] Genetisch onderzoek sectie uitbreiden
- [ ] Foto's/beeldmateriaal toevoegen (medische illustraties)

## Let op
- Port 8093 (geen conflict met andere projecten)
- Wetenschappelijk taalgebruik, geen emoji's
- Evidence-based: alle claims met bronvermelding
- Geen frameworks, pure HTML/CSS/JS
- `serve.py` is een simpele Python HTTP server (geen Flask)
