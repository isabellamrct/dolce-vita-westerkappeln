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

## ⚠️ Vor dem Veröffentlichen prüfen

Die Bewertungsportale (Tripadvisor, Google, Restaurant Guru, Facebook) waren bei der Erstellung nicht direkt abrufbar. Folgendes muss mit dem Restaurant abgeglichen werden:

1. **Speisekarte & Preise** – Gerichte und Preise sind eine realistische Vorlage im Stil einer italienischen Pizzeria im Münsterland, **nicht** die echte Karte. Bitte vollständig mit der aktuellen Karte ersetzen (`MENU` und `DRINKS` in `build.py`).
2. **Öffnungszeiten** – Quellen widersprechen sich. Verwendet: Mo Ruhetag, Di–Sa 12:00–14:30 & 17:00–22:00, So 13:00–22:00.
3. **Bewertungen** – Tripadvisor 5,0 von 5 ist belegt. Die Zitate stammen aus Suchergebnis-Auszügen der Tripadvisor-Bewertungen und sind teils gekürzt/sinngemäß. Bitte den genauen Wortlaut auf Tripadvisor prüfen und echte Google-Rezensionen ergänzen (`REVIEWS` in `build.py`). Die Google-Gesamtnote ist bewusst nicht angegeben, bis sie bestätigt ist.
4. **Über uns** – Texte sind allgemein gehalten. Abholung ist bestätigt; Angaben zu Feiern/Gruppen bestätigen lassen und gern mit der echten Geschichte (Inhaber, seit wann) ergänzen.
5. **Impressum & Datenschutz** – gelb markierte Platzhalter (Inhaber, E-Mail, USt-IdNr., Hoster) ausfüllen.
6. **Fotos** – sobald eigene Fotos vorliegen (Speisen, Gastraum), in `img/` ablegen und einbinden. Bewusst keine Stockfotos.
7. **Schriften** – für maximale DSGVO-Sicherheit Cormorant Garamond und Work Sans lokal hosten (z. B. via google-webfonts-helper) und den `@import` in `css/style.css` ersetzen.

## Lokal ansehen

```bash
python3 -m http.server 8000
# dann http://localhost:8000 öffnen
```
