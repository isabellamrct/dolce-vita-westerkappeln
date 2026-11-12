# Dolce Vita Westerkappeln – Website

Statische, mehrseitige Website für das Ristorante & Pizzeria **Dolce Vita**, Vidumstraße 1, 49492 Westerkappeln.
Kein Framework, keine Cookies, kein Tracking – läuft auf jedem einfachen Webhosting.

## Seiten

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Begrüßung, Öffnungszeiten mit „Jetzt geöffnet“-Anzeige, Empfehlungen, Bewertungen |
| `speisekarte.html` | Komplette Speisekarte mit Preisen und Getränkekarte, Rubrik-Navigation |
| `ueber-uns.html` | Restaurant, Feiern & Gruppen, Abholung, Lage im Tecklenburger Land |
| `bewertungen.html` | Gästestimmen von Tripadvisor, Links zu Google & Tripadvisor |
| `kontakt.html` | Adresse, Telefon, Öffnungszeiten, Anfahrt |
| `impressum.html`, `datenschutz.html` | Rechtliches (Platzhalter ausfüllen!) |

## Inhalte ändern

Alle Seiten werden aus **`build.py`** erzeugt. Speisekarte, Preise, Bewertungen und Texte dort ändern, dann:

```bash
python3 build.py
```

Die Öffnungszeiten stehen an zwei Stellen: in `build.py` (Tabelle, Fußzeile, Google-Daten) und in `js/main.js` (Live-Anzeige „geöffnet/geschlossen“).

## Veröffentlichen

Die Website besteht nur aus statischen Dateien. Den kompletten Ordner (ohne `.git`, `build.py` und `README.md`) per FTP auf den Webspace hochladen, z. B. bei IONOS, Strato oder All-Inkl. Alternativ kostenlos über GitHub Pages (`.nojekyll` und `404.html` sind vorhanden) oder Netlify.

- Schriften sind lokal eingebunden (`fonts/`), es werden **keine** Cookies gesetzt und keine externen Dienste geladen.
- `robots.txt` erlaubt die Indexierung. Nach dem Livegang die Website-Adresse im Google-Unternehmensprofil, bei Tripadvisor, Instagram und Facebook eintragen.

## ⚠️ Vor dem Livegang ausfüllen bzw. prüfen

1. **Impressum & Datenschutz** – gelb markierte Platzhalter (Inhaber, E-Mail, USt-IdNr., Hoster). **Ohne vollständiges Impressum nicht veröffentlichen.**
2. **Speisekarte & Preise** – Instagram und Google waren nicht abrufbar (Login bzw. Sperre). Gerichte und Preise sind eine Vorlage im Stil der Pizzeria, **nicht** die echte Karte. Mit der aktuellen Karte abgleichen (`MENU` und `DRINKS` in `build.py`), dann `python3 build.py`.
3. **Bewertungen** – auf der Seite stehen nur wörtlich belegte Zitate (Tripadvisor, TikTok @umuditestet). Weitere Google-Rezensionen können in `REVIEWS` ergänzt werden – am besten mit Vorname + Initial und nur mit wörtlichem Text.
4. **Fotos** – eigene Fotos (Instagram des Restaurants) können in `img/` abgelegt und eingebunden werden. Keine Gästefotos von Google ohne Erlaubnis verwenden (Urheberrecht).

Bestätigt: Öffnungszeiten, Telefonnummer, Abholung. Keine glutenfreie Pasta.

## Lokal ansehen

```bash
python3 -m http.server 8000
# dann http://localhost:8000 öffnen
```
