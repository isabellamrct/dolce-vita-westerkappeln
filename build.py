#!/usr/bin/env python3
"""Erzeugt die statischen HTML-Seiten für Dolce Vita Westerkappeln."""
import sys, os, html

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

PHONE = "05404 7009405"
PHONE_LINK = "+4954047009405"
ADDR1 = "Vidumstraße 1"
ADDR2 = "49492 Westerkappeln"
MAPS = "https://www.google.com/maps/search/?api=1&query=Dolce+Vita+Vidumstra%C3%9Fe+1+49492+Westerkappeln"
ROUTE = "https://www.google.com/maps/dir/?api=1&destination=Vidumstra%C3%9Fe+1%2C+49492+Westerkappeln"
OSM = "https://www.openstreetmap.org/search?query=Vidumstra%C3%9Fe%201%2C%2049492%20Westerkappeln"
TRIP = "https://www.tripadvisor.de/Restaurant_Review-g3331348-d24987084-Reviews-Dolce_vita-Westerkappeln_North_Rhine_Westphalia.html"
FB = "https://www.facebook.com/p/Dolce-vita-100069733084038/"
IG = "https://www.instagram.com/dolcevita_westerkappeln/"
TT = "https://www.tiktok.com/@umuditestet/video/7616672092297170198"

NAV = [
    ("index.html", "Start"),
    ("speisekarte.html", "Speisekarte"),
    ("ueber-uns.html", "Über uns"),
    ("bewertungen.html", "Bewertungen"),
    ("kontakt.html", "Kontakt"),
]

HOURS_ROWS = """<table class="hours">
          <tr data-day="1"><th>Montag</th><td>Ruhetag</td></tr>
          <tr data-day="2,3,4,5,6"><th>Dienstag – Samstag</th><td>12:00 – 14:30<br>17:00 – 22:00</td></tr>
          <tr data-day="0"><th>Sonntag &amp; Feiertage</th><td>13:00 – 22:00</td></tr>
        </table>"""

OLIVE_SVG = """<svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M4 26C12 22 20 14 28 4"/><path d="M10 22c-3-1-5-4-5-7 3 0 6 2 7 5"/><path d="M16 16c1-3 4-5 7-5 0 3-2 6-5 7"/><path d="M14 18c-3-1-5-4-5-7 3 0 6 2 7 5"/><ellipse cx="21" cy="21" rx="3" ry="4" transform="rotate(-30 21 21)" fill="currentColor" stroke="none"/></svg>"""


def head(title, desc, extra=""):
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#36432b">
<meta property="og:type" content="restaurant">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="de_DE">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="css/style.css">
{extra}</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
"""


def header(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    items.append(f'<li><a class="btn btn-small" href="tel:{PHONE_LINK}">Tisch reservieren</a></li>')
    return f"""<div class="topbar">
  <div class="wrap">
    <span data-status>{ADDR1} · Westerkappeln</span>
    <span><a href="tel:{PHONE_LINK}">Telefon {PHONE}</a></span>
  </div>
</div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Dolce Vita – zur Startseite">
      <span class="brand-name">Dolce Vita</span>
      <span class="brand-sub">Ristorante · Pizzeria · Westerkappeln</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menü</button>
    <nav class="nav" id="nav" aria-label="Hauptnavigation">
      <ul>
        {"".join(items)}
      </ul>
    </nav>
  </div>
</header>
<main id="inhalt">
"""


def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <span class="brand-name" style="font-family:var(--serif);font-style:italic;font-weight:600">Dolce Vita</span>
        <p style="margin-top:.6rem">Ristorante &amp; Pizzeria an der Vidumstraße in Westerkappeln.</p>
      </div>
      <div>
        <h4>Besuchen</h4>
        <p>{ADDR1}<br>{ADDR2}<br><a href="{ROUTE}" rel="noopener">Route planen</a></p>
      </div>
      <div>
        <h4>Öffnungszeiten</h4>
        <p>Mo Ruhetag<br>Di – Sa 12:00 – 14:30<br>&amp; 17:00 – 22:00<br>So 13:00 – 22:00</p>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li><a href="tel:{PHONE_LINK}">{PHONE}</a></li>
          <li><a href="{IG}" rel="noopener">Instagram</a></li>
          <li><a href="{FB}" rel="noopener">Facebook</a></li>
          <li><a href="{TRIP}" rel="noopener">Tripadvisor</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> Dolce Vita Westerkappeln</span>
      <span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def cta():
    return f"""<section class="section section-dark cta-band">
  <div class="wrap">
    <h2>Reservieren oder zum Abholen bestellen</h2>
    <p>Einfach anrufen – wir nehmen Ihre Reservierung oder Bestellung gern telefonisch entgegen.</p>
    <a class="phone-big" href="tel:{PHONE_LINK}">{PHONE}</a>
  </div>
</section>
"""


def page(name, title, desc, active, body, extra=""):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(head(title, desc, extra) + header(active) + body + footer())


# ------------------------------------------------------------------ Speisekarte
# Format: (Nr, Name, Beschreibung, Preis, Badge)  Badge: "veg" | "house" | None
MENU = [
    ("antipasti", "Antipasti", "Zum Anfangen – oder zum Teilen in der Tischmitte.", [
        ("1", "Pane all'aglio", "Pizzabrot mit Knoblauch, Olivenöl und Rosmarin", "5,00", "veg"),
        ("2", "Bruschetta classica", "Geröstetes Brot mit Tomaten, Basilikum, Knoblauch und Olivenöl", "6,90", "veg"),
        ("3", "Insalata Caprese", "Tomaten, Fior di Latte, Basilikum, Olivenöl extra vergine", "10,90", "veg"),
        ("4", "Carpaccio di manzo", "Hauchdünnes Rinderfilet mit Rucola, Parmesan und Zitrone", "13,90", None),
        ("5", "Vitello tonnato", "Kalbfleisch in feinen Scheiben mit Thunfisch-Kapern-Sauce", "13,50", None),
        ("6", "Gamberoni aglio e olio", "Riesengarnelen in Knoblauch, Olivenöl und Peperoncino, dazu Brot", "14,50", None),
        ("7", "Antipasto misto della casa", "Gemischte Vorspeisenplatte nach Tagesangebot – für zwei Personen", "19,90", "house"),
    ]),
    ("zuppe", "Zuppe &amp; Insalate", "Salate auf Wunsch mit Haus-Dressing oder Balsamico und Olivenöl.", [
        ("10", "Minestrone", "Italienische Gemüsesuppe", "6,50", "veg"),
        ("11", "Crema di pomodoro", "Tomatencremesuppe mit Sahnehaube und Basilikum", "6,50", "veg"),
        ("12", "Insalata mista", "Gemischter Salat der Saison", "6,50", "veg"),
        ("13", "Insalata di rucola", "Rucola, Kirschtomaten, gehobelter Parmesan", "10,90", "veg"),
        ("14", "Insalata tonno", "Gemischter Salat mit Thunfisch, Zwiebeln, Oliven und Ei", "12,50", None),
        ("15", "Insalata Dolce Vita", "Bunter Salat mit gebratenen Putenbruststreifen und Champignons", "13,90", "house"),
    ]),
    ("pizza", "Pizze", "Dünn ausgerollter Teig, lange gereift. Alle Pizzen mit Tomatensauce und Mozzarella, Ø ca. 30 cm.", [
        ("20", "Margherita", "Tomaten, Mozzarella, Basilikum", "9,50", "veg"),
        ("21", "Funghi", "Frische Champignons", "10,50", "veg"),
        ("22", "Salame", "Italienische Salami", "10,90", None),
        ("23", "Prosciutto", "Gekochter Schinken", "10,90", None),
        ("24", "Tonno", "Thunfisch und rote Zwiebeln", "11,90", None),
        ("25", "Hawaii", "Schinken und Ananas", "11,50", None),
        ("26", "Vegetariana", "Paprika, Zucchini, Aubergine, Champignons, Spinat", "12,50", "veg"),
        ("27", "Diavola", "Scharfe Salami, Peperoncino, Zwiebeln", "12,50", None),
        ("28", "Quattro stagioni", "Schinken, Salami, Champignons, Artischocken", "12,50", None),
        ("29", "Calzone", "Gefüllt mit Schinken, Salami, Champignons und Ricotta", "12,90", None),
        ("30", "Bufala", "Büffelmozzarella, Kirschtomaten, Basilikum – nach dem Backen belegt", "13,90", "veg"),
        ("31", "Rucola e Parma", "Rucola, Parmaschinken, Parmesan – nach dem Backen belegt", "14,50", None),
        ("32", "Frutti di mare", "Meeresfrüchte, Knoblauch, Petersilie", "14,90", None),
        ("33", "Pizza Dolce Vita", "Unsere Hauspizza: Salsiccia, Friarielli, Fior di Latte, Parmesan", "14,90", "house"),
    ]),
    ("pasta", "Pasta &amp; Risotto", "", [
        ("40", "Spaghetti al pomodoro", "Tomatensauce und Basilikum", "9,90", "veg"),
        ("41", "Spaghetti aglio, olio e peperoncino", "Knoblauch, Olivenöl, Chili, Petersilie", "10,50", "veg"),
        ("42", "Penne all'arrabbiata", "Pikante Tomatensauce mit Knoblauch und Chili", "10,90", "veg"),
        ("43", "Spaghetti bolognese", "Hausgemachtes Rinderragù", "11,50", None),
        ("44", "Spaghetti carbonara", "Guanciale, Eigelb, Pecorino, schwarzer Pfeffer – ohne Sahne", "12,50", None),
        ("45", "Tortellini alla panna", "Sahnesauce mit Schinken und Erbsen", "12,50", None),
        ("46", "Gnocchi alla sorrentina", "Tomatensauce, Mozzarella, Basilikum, im Ofen überbacken", "12,50", "veg"),
        ("47", "Lasagne al forno", "Nach Hausrezept, im Ofen überbacken", "12,90", "house"),
        ("48", "Tagliatelle ai funghi", "Champignons und Steinpilze in Sahnesauce", "12,90", "veg"),
        ("49", "Tagliatelle al salmone", "Lachs in Tomaten-Sahnesauce mit Dill", "14,90", None),
        ("50", "Risotto ai porcini", "Cremiges Risotto mit Steinpilzen und Parmesan", "15,90", "veg"),
        ("51", "Spaghetti frutti di mare", "Meeresfrüchte in Weißwein, Knoblauch und Kirschtomaten", "16,90", None),
    ]),
    ("carne", "Carne &amp; Pesce", "Fleisch- und Fischgerichte mit Beilage nach Wahl: Rosmarinkartoffeln, Pasta oder Gemüse – dazu ein kleiner Salat.", [
        ("60", "Pollo alla griglia", "Gegrillte Hähnchenbrust mit Kräutern", "17,50", None),
        ("61", "Cotoletta alla milanese", "Paniertes Schweineschnitzel nach Mailänder Art", "17,90", None),
        ("62", "Scaloppine al limone", "Kalbsschnitzel in Zitronen-Weißwein-Sauce", "19,90", None),
        ("63", "Saltimbocca alla romana", "Kalbsschnitzel mit Parmaschinken und Salbei", "21,90", "house"),
        ("64", "Filetto al pepe verde", "Rinderfilet (ca. 200 g) mit grüner Pfeffersauce", "29,90", None),
        ("65", "Salmone alla griglia", "Gegrilltes Lachsfilet mit Zitronenbutter", "21,50", None),
        ("66", "Orata al forno", "Doradenfilet aus dem Ofen mit Kirschtomaten und Oliven", "22,90", None),
        ("67", "Gamberoni alla griglia", "Gegrillte Riesengarnelen mit Knoblauchöl", "24,90", None),
    ]),
    ("kinder", "Für Kinder", "Bis 12 Jahre.", [
        ("70", "Piccola Margherita", "Kleine Pizza mit Tomaten und Mozzarella", "7,00", "veg"),
        ("71", "Spaghetti bolognese, kleine Portion", "", "7,50", None),
        ("72", "Kinderschnitzel mit Pommes frites", "", "8,50", None),
    ]),
    ("dolci", "Dolci", "Hausgemacht, solange der Vorrat reicht.", [
        ("80", "Affogato al caffè", "Vanilleeis mit heißem Espresso", "5,50", "veg"),
        ("81", "Gelato misto", "Drei Kugeln Eis nach Wahl, mit Sahne", "5,90", "veg"),
        ("82", "Panna cotta", "Mit Beerensauce", "6,50", "veg"),
        ("83", "Tiramisù della casa", "Nach dem Rezept des Hauses", "6,90", "house"),
        ("84", "Tartufo", "Schokoladen-Eistrüffel", "6,90", "veg"),
    ]),
]

DRINKS = [
    ("aperitivo", "Aperitivi", "", [
        ("Prosecco", "0,1 l", "5,50"),
        ("Aperol Spritz", "0,2 l", "7,50"),
        ("Hugo", "0,2 l", "7,50"),
        ("Campari Orange", "4 cl", "7,00"),
        ("Crodino (alkoholfrei)", "0,1 l", "4,50"),
    ]),
    ("wein", "Vini", "Offene Weine. Unsere Flaschenweine empfehlen wir Ihnen gern am Tisch.", [
        ("Pinot Grigio delle Venezie – weiß, trocken", "0,2 l", "6,50"),
        ("Lugana – weiß, trocken", "0,2 l", "7,50"),
        ("Rosato di Puglia – rosé", "0,2 l", "6,50"),
        ("Montepulciano d'Abruzzo – rot, trocken", "0,2 l", "6,50"),
        ("Primitivo di Manduria – rot, kräftig", "0,2 l", "7,50"),
        ("Hauswein rot oder weiß", "1,0 l Karaffe", "22,00"),
    ]),
    ("bier", "Birre", "", [
        ("Pils vom Fass", "0,3 l / 0,5 l", "3,60 / 4,90"),
        ("Peroni Nastro Azzurro", "0,33 l", "4,20"),
        ("Hefeweizen", "0,5 l", "4,90"),
        ("Alkoholfreies Bier", "0,33 l", "3,90"),
        ("Radler", "0,3 l / 0,5 l", "3,60 / 4,90"),
    ]),
    ("softdrinks", "Analcolici", "", [
        ("Mineralwasser still oder sprudelnd", "0,25 l / 0,75 l", "2,90 / 6,50"),
        ("Cola, Cola light, Fanta, Sprite", "0,2 l / 0,4 l", "2,90 / 4,50"),
        ("San Pellegrino Limonata oder Aranciata", "0,33 l", "3,90"),
        ("Apfelschorle", "0,2 l / 0,4 l", "2,90 / 4,50"),
        ("Säfte: Apfel, Orange, Maracuja", "0,2 l", "3,20"),
    ]),
    ("caffe", "Caffè", "", [
        ("Espresso", "", "2,40"),
        ("Doppio", "", "3,60"),
        ("Caffè crema", "", "3,00"),
        ("Cappuccino", "", "3,40"),
        ("Latte macchiato", "", "3,80"),
        ("Tee nach Wahl", "", "2,90"),
    ]),
    ("digestivo", "Digestivi", "", [
        ("Limoncello", "2 cl", "3,50"),
        ("Amaro Montenegro / Averna / Ramazzotti", "4 cl", "4,50"),
        ("Sambuca", "2 cl", "3,50"),
        ("Grappa di Prosecco", "2 cl", "4,00"),
        ("Grappa barrique", "2 cl", "5,50"),
    ]),
]


def dish_html(no, name, desc, price, badge):
    b = ""
    if badge == "veg":
        b = '<span class="badge veg" title="vegetarisch">veg.</span>'
    elif badge == "house":
        b = '<span class="badge house">Hausrezept</span>'
    d = f"<p>{desc}</p>" if desc else ""
    return f"""        <div class="dish">
          <span class="no">{no}</span>
          <div><h3>{name}{b}</h3>{d}</div>
          <span class="price">{price} €</span>
        </div>
"""


def drink_html(name, size, price):
    d = f"<p>{size}</p>" if size else ""
    return f"""        <div class="dish">
          <span class="no"></span>
          <div><h3>{name}</h3>{d}</div>
          <span class="price">{price} €</span>
        </div>
"""


def menu_page():
    nav = []
    secs = []
    for sid, title, intro, dishes in MENU:
        nav.append(f'<li><a href="#{sid}">{title}</a></li>')
        rows = "".join(dish_html(*d) for d in dishes)
        extra = ""
        if sid == "pizza":
            extra = '        <p style="margin:1rem 0 0;font-size:.92rem;color:var(--ink-soft)">Jede weitere Zutat 1,50 € · Büffelmozzarella oder Parmaschinken 2,50 €</p>\n'
        secs.append(f"""      <section class="menu-section" id="{sid}">
        <header><h2>{title}</h2>{"<p>" + intro + "</p>" if intro else ""}</header>
{rows}{extra}      </section>
""")
    nav.append('<li><a href="#getraenke">Getränke</a></li>')
    drink_secs = []
    for sid, title, intro, items in DRINKS:
        rows = "".join(drink_html(*i) for i in items)
        ip = f'<p style="color:var(--ink-soft);font-size:.95rem;margin:0 0 .6rem">{intro}</p>' if intro else ""
        drink_secs.append(f"""        <h3 style="margin-top:2rem" id="{sid}">{title}</h3>{ip}
{rows}""")
    secs.append(f"""      <section class="menu-section" id="getraenke">
        <header><h2>Getränke</h2><p>Von Aperitivo bis Digestivo.</p></header>
{"".join(drink_secs)}      </section>
""")

    body = f"""<section class="page-head">
  <div class="wrap">
    <h1>Speisekarte</h1>
    <p>Alle Gerichte auch zum Abholen – telefonisch bestellen unter <a href="tel:{PHONE_LINK}">{PHONE}</a>. Neues und Aktionen zeigen wir auf <a href="{IG}" rel="noopener">Instagram</a>.</p>
  </div>
</section>

<!-- HINWEIS: Gerichte und Preise mit der aktuellen Karte des Restaurants abgleichen (siehe README). -->
<section class="section" style="padding-top:3rem">
  <div class="wrap menu-layout">
    <nav class="menu-nav" aria-label="Rubriken der Speisekarte">
      <ol>
        {"".join(nav)}
      </ol>
    </nav>
    <div>
{"".join(secs)}
      <div class="menu-note">
        <p><strong>Allergene &amp; Zusatzstoffe:</strong> Informationen zu Allergenen und kennzeichnungspflichtigen Zusatzstoffen erhalten Sie jederzeit bei unserem Service-Team. Bei Unverträglichkeiten sprechen Sie uns bitte vor der Bestellung an.</p>
        <p>Alle Preise in Euro inklusive der gesetzlichen Mehrwertsteuer. Irrtümer und Änderungen vorbehalten.</p>
      </div>
    </div>
  </div>
</section>
""" + cta()
    page("speisekarte.html", "Speisekarte – Dolce Vita Westerkappeln",
         "Speisekarte mit Preisen: Pizza, Pasta, Antipasti, Fleisch, Fisch und Dolci im Dolce Vita, Vidumstraße 1 in Westerkappeln.",
         "speisekarte.html", body)


# ------------------------------------------------------------------ Bewertungen
REVIEWS = [
    ("Klein aber fein … Gehobene Küche, gut getarnt.", "Tripadvisor", "Gästebewertung", TRIP),
    ("Bestes Restaurant in Westerkappeln", "Tripadvisor", "Gästebewertung", "https://www.tripadvisor.de/ShowUserReviews-g3331348-d24987084-r861253359-Dolce_vita-Westerkappeln_North_Rhine_Westphalia.html"),
    ("Das war absolut lecker", "TikTok", "@umuditestet", TT),
]

# Was Gäste in ihren Bewertungen hervorheben (Zusammenfassung, keine wörtlichen Zitate)
PRAISE = [
    ("Mehr als eine Pizzeria", "Gäste beschreiben die Küche als fein und kreativ – deutlich mehr als eine klassische Pizzeria."),
    ("Faire Preise", "Mehrfach gelobt: das Preis-Leistungs-Verhältnis. Ein Gast nennt das Dolce Vita einen echten Insidertipp."),
    ("Aufmerksamer Service", "Das Essen sei immer sehr gut, die Bedienung aufmerksam – auch Gäste aus Osnabrück kommen gern wieder."),
]


def quotes_block(items):
    out = []
    for q, src, note, url in items:
        out.append(f"""      <figure class="quote">
        <blockquote>{q}</blockquote>
        <figcaption>{note} · <a href="{url}" rel="noopener">{src}</a></figcaption>
      </figure>
""")
    return "".join(out)


def ratings_row():
    return f"""<div class="rating-row">
      <div class="rating">
        <span class="score">5,0</span>
        <span class="meta"><span class="stars" aria-label="5 von 5 Punkten">★★★★★</span><strong>Tripadvisor</strong><a href="{TRIP}" rel="noopener">Alle Bewertungen lesen</a></span>
      </div>
      <div class="rating" style="align-self:center">
        <span class="meta"><strong>Google-Rezensionen</strong><a href="{MAPS}" rel="noopener">Bewertungen auf Google lesen</a></span>
      </div>
    </div>"""


# ------------------------------------------------------------------ Seiten
def index_page():
    schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Dolce Vita",
  "servesCuisine": ["Italienisch", "Pizza", "Pasta"],
  "telephone": "{PHONE_LINK}",
  "priceRange": "€€",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{ADDR1}",
    "postalCode": "49492",
    "addressLocality": "Westerkappeln",
    "addressRegion": "Nordrhein-Westfalen",
    "addressCountry": "DE"
  }},
  "openingHoursSpecification": [
    {{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "12:00", "closes": "14:30"}},
    {{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "17:00", "closes": "22:00"}},
    {{"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "13:00", "closes": "22:00"}}
  ],
  "hasMenu": "speisekarte.html",
  "acceptsReservations": "True",
  "sameAs": ["{IG}", "{FB}", "{TRIP}"]
}}
</script>
"""

    cats = [
        ("antipasti", "Antipasti", "Bruschetta, Carpaccio, Vitello tonnato"),
        ("pizza", "Pizze", "Klassiker und Pizza Dolce Vita"),
        ("pasta", "Pasta &amp; Risotto", "Von Aglio e olio bis Frutti di mare"),
        ("carne", "Carne &amp; Pesce", "Saltimbocca, Filetto, Fisch vom Grill"),
        ("dolci", "Dolci", "Tiramisù, Panna cotta, Affogato"),
        ("getraenke", "Getränke", "Aperitivo, offene Weine, Caffè"),
    ]
    cat_html = "".join(f"""      <li><a href="speisekarte.html#{a}"><span class="cat-name">{n}</span><span class="cat-desc">{d}</span></a></li>
""" for a, n, d in cats)

    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="hero-place">{ADDR1} · Westerkappeln</p>
      <h1>Pizza, Pasta und italienische Küche – <em>mitten im Ort.</em></h1>
      <p class="lead">Ristorante und Pizzeria im Ortskern von Westerkappeln. Mittags und abends geöffnet, montags Ruhetag. Alles von der Karte gibt es auch zum Abholen.</p>
      <div class="hero-actions">
        <a class="btn" href="tel:{PHONE_LINK}">Anrufen: {PHONE}</a>
        <a class="btn btn-ghost" href="speisekarte.html">Speisekarte</a>
      </div>
    </div>
    <aside class="hero-card" aria-labelledby="oz">
      <h2 id="oz">Öffnungszeiten</h2>
      {HOURS_ROWS}
      <p class="small" data-status></p>
    </aside>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="split-head">
      <h2>Aus der Karte</h2>
      <a href="speisekarte.html">Ganze Speisekarte mit Preisen</a>
    </div>
    <ul class="cat-list">
{cat_html}    </ul>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <h2 style="margin-bottom:2.2rem">Was Gäste sagen</h2>
    <div class="quotes">
{quotes_block(REVIEWS)}    </div>
    <p style="margin-top:2.2rem"><a href="bewertungen.html">Mehr Bewertungen</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div>
      <h2>Zum Abholen</h2>
      <p style="color:var(--ink-soft)">Rufen Sie an, bestellen Sie von der Karte und holen Sie Ihr Essen zur vereinbarten Zeit an der Vidumstraße ab.</p>
      <p><a class="btn btn-ghost" href="tel:{PHONE_LINK}">{PHONE}</a></p>
    </div>
    <div>
      <h2>Anfahrt</h2>
      <p style="color:var(--ink-soft)">{ADDR1}, {ADDR2} – im Ortskern, wenige Minuten vom Lotter Kreuz und rund 20 Minuten von Osnabrück.</p>
      <p><a class="btn btn-ghost" href="{ROUTE}" rel="noopener">Route planen</a></p>
    </div>
  </div>
</section>
"""
    page("index.html", "Dolce Vita – Ristorante & Pizzeria in Westerkappeln",
         "Italienisches Restaurant und Pizzeria im Ortskern von Westerkappeln. Pizza, Pasta, Fleisch und Fisch – Vidumstraße 1, Telefon 05404 7009405.",
         "index.html", body, schema)


def about_page():
    body = f"""<section class="page-head">
  <div class="wrap">
    <h1>Über uns</h1>
    <p>Ein kleines italienisches Restaurant an der Vidumstraße, mitten in Westerkappeln.</p>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div class="prose">
      <h2>Klein aber fein.</h2>
      <p class="drop">So hat ein Gast auf Tripadvisor das Dolce Vita beschrieben, und das trifft es. Das Restaurant liegt im Ortskern von Westerkappeln, an der Vidumstraße. Hierher kommen Gäste aus dem Ort, aus dem Tecklenburger Land und aus Osnabrück.</p>
      <p>Auf der Karte stehen Pizza, Pasta und Risotto, Fleisch- und Fischgerichte, Antipasti und Dolci. Dazu italienische Weine, Aperitivo und Espresso.</p>
      <p>Was es aktuell Neues gibt, zeigen wir auf <a href="{IG}" rel="noopener">Instagram</a>.</p>
    </div>
    <div>
      <div class="rule">{OLIVE_SVG}</div>
      <h3>Für Familienfeiern &amp; Gruppen</h3>
      <p style="color:var(--ink-soft)">Sie planen einen Abend mit Familie, Freunden oder Kollegen? Rufen Sie uns an, dann besprechen wir, was möglich ist.</p>
      <h3 style="margin-top:2rem">Zum Abholen</h3>
      <p style="color:var(--ink-soft)">Alle Gerichte der Karte können Sie telefonisch unter <a href="tel:{PHONE_LINK}">{PHONE}</a> bestellen und zur vereinbarten Zeit bei uns abholen.</p>
      <h3 style="margin-top:2rem">Vegetarisch</h3>
      <p style="color:var(--ink-soft)">Vegetarische Gerichte sind auf der Speisekarte gekennzeichnet. Bei Allergien und Unverträglichkeiten sprechen Sie uns bitte vor der Bestellung an.</p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Zwischen Münsterland und Osnabrücker Land</h2>
      <p>Westerkappeln liegt am Rand des Tecklenburger Landes, nur wenige Minuten vom Lotter Kreuz und von Osnabrück entfernt. Ob nach einer Radtour am Mittellandkanal, einem Spaziergang durch den Ortskern oder auf dem Heimweg von der Arbeit – bei uns kehren Sie ganz unkompliziert ein.</p>
    </div>
    <a class="btn btn-ghost" href="kontakt.html">Anfahrt &amp; Kontakt</a>
  </div>
</section>
""" + cta()
    page("ueber-uns.html", "Über uns – Dolce Vita Westerkappeln",
         "Das Dolce Vita ist ein kleines italienisches Restaurant im Ortskern von Westerkappeln: frische Küche, Familienfeiern, Speisen zum Abholen.",
         "ueber-uns.html", body)


def reviews_page():
    cards = "".join(f"""      <article class="review">
        <div class="review-head">
          <span class="source"><a href="{url}" rel="noopener">{src}</a></span>
          <span style="font-size:.85rem;color:var(--ink-soft)">{note}</span>
        </div>
        <h3>„{q}“</h3>
      </article>
""" for q, src, note, url in REVIEWS)
    praise = "".join(f"""      <div>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>
""" for t, d in PRAISE)
    body = f"""<section class="page-head">
  <div class="wrap">
    <h1>Bewertungen</h1>
    <p>Danke an alle, die sich die Zeit nehmen, über ihren Besuch zu schreiben.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {ratings_row()}
    <div class="review-list">
{cards}    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <h2 style="margin-bottom:2rem">Was Gäste besonders hervorheben</h2>
    <div class="info-grid">
{praise}    </div>
    <div class="menu-note" style="margin-top:2.5rem">
      <p>Zusammengefasst aus Bewertungen auf Tripadvisor. Alle Bewertungen im Original finden Sie auf <a href="{MAPS}" rel="noopener">Google</a> und <a href="{TRIP}" rel="noopener">Tripadvisor</a> – dort freuen wir uns auch über Ihre.</p>
    </div>
  </div>
</section>
""" + cta()
    page("bewertungen.html", "Bewertungen – Dolce Vita Westerkappeln",
         "Gästebewertungen des Dolce Vita in Westerkappeln: 5,0 von 5 auf Tripadvisor.",
         "bewertungen.html", body)


def contact_page():
    body = f"""<section class="page-head">
  <div class="wrap">
    <h1>Kontakt &amp; Anfahrt</h1>
    <p>Reservierungen und Bestellungen zum Abholen nehmen wir telefonisch entgegen.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="info-grid">
      <div>
        <h3>Adresse</h3>
        <address>Dolce Vita<br>{ADDR1}<br>{ADDR2}</address>
        <p style="margin-top:1rem"><a class="btn btn-small" href="{ROUTE}" rel="noopener">Route planen</a></p>
      </div>
      <div>
        <h3>Telefon</h3>
        <p><a href="tel:{PHONE_LINK}" style="font-size:1.3rem;font-weight:600;text-decoration:none">{PHONE}</a></p>
        <p>Am besten erreichen Sie uns während der Öffnungszeiten. Für Gruppen ab acht Personen bitten wir um Reservierung einige Tage im Voraus.</p>
      </div>
      <div>
        <h3>Öffnungszeiten</h3>
        {HOURS_ROWS}
        <p style="margin-top:.8rem;font-size:.9rem" data-status></p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap two-col">
    <div>
      <h2>Anfahrt</h2>
      <p style="color:var(--ink-soft)">Das Restaurant liegt im Ortskern von Westerkappeln. Parkmöglichkeiten finden Sie in den umliegenden Straßen und auf den öffentlichen Parkplätzen im Zentrum.</p>
      <p><a href="{MAPS}" rel="noopener">In Google Maps öffnen</a> · <a href="{OSM}" rel="noopener">In OpenStreetMap öffnen</a></p>
    </div>
    <ol class="steps">
      <li><strong>Aus Osnabrück</strong>Richtung Westen über Lotte nach Westerkappeln, ca. 20 Minuten.</li>
      <li><strong>Über die Autobahn</strong>A1 oder A30 bis zum Lotter Kreuz, von dort wenige Minuten bis in den Ortskern.</li>
      <li><strong>Aus Ibbenbüren, Mettingen &amp; Recke</strong>Über die Landstraßen des Tecklenburger Landes direkt in die Ortsmitte.</li>
    </ol>
  </div>
</section>
""" + cta()
    page("kontakt.html", "Kontakt & Anfahrt – Dolce Vita Westerkappeln",
         "Dolce Vita, Vidumstraße 1, 49492 Westerkappeln. Telefon 05404 7009405. Öffnungszeiten, Anfahrt und Reservierung.",
         "kontakt.html", body)


T = '<span class="todo">'
E = "</span>"


def impressum_page():
    body = f"""<section class="page-head">
  <div class="wrap"><h1>Impressum</h1></div>
</section>
<section class="section">
  <div class="wrap legal">
    <h2>Angaben gemäß § 5 DDG</h2>
    <p>Dolce Vita<br>Inhaber: {T}[Vor- und Nachname des Inhabers]{E}<br>{ADDR1}<br>{ADDR2}</p>
    <h3>Kontakt</h3>
    <p>Telefon: {PHONE}<br>E-Mail: {T}[E-Mail-Adresse]{E}</p>
    <h3>Umsatzsteuer-ID</h3>
    <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: {T}[USt-IdNr., falls vorhanden]{E}</p>
    <h3>Verantwortlich für den Inhalt</h3>
    <p>{T}[Vor- und Nachname]{E}, Anschrift wie oben.</p>
    <h3>Verbraucherstreitbeilegung</h3>
    <p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
    <h3>Haftung für Inhalte und Links</h3>
    <p>Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte – insbesondere der Speisekarte und der Preise – können wir jedoch keine Gewähr übernehmen. Für die Inhalte verlinkter externer Seiten sind ausschließlich deren Betreiber verantwortlich.</p>
  </div>
</section>
"""
    page("impressum.html", "Impressum – Dolce Vita Westerkappeln", "Impressum des Restaurants Dolce Vita in Westerkappeln.", None, body,
         '<meta name="robots" content="noindex">\n')


def datenschutz_page():
    body = f"""<section class="page-head">
  <div class="wrap"><h1>Datenschutzerklärung</h1></div>
</section>
<section class="section">
  <div class="wrap legal">
    <h2>1. Verantwortlicher</h2>
    <p>Dolce Vita, {T}[Inhaber]{E}, {ADDR1}, {ADDR2}, Telefon {PHONE}, E-Mail {T}[E-Mail-Adresse]{E}.</p>

    <h2>2. Hosting und Server-Logfiles</h2>
    <p>Beim Aufruf dieser Website werden durch den Hosting-Anbieter {T}[Name und Anschrift des Hosters]{E} automatisch Informationen in Server-Logfiles gespeichert, die Ihr Browser übermittelt (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Referrer, Browser und Betriebssystem). Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO; unser berechtigtes Interesse liegt im sicheren und stabilen Betrieb der Website. Die Daten werden nach {T}[x]{E} Tagen gelöscht.</p>

    <h2>3. Schriftarten</h2>
    <p>Die verwendeten Schriftarten sind lokal auf unserem Server gespeichert. Beim Aufruf der Website wird keine Verbindung zu Servern Dritter (z. B. Google) hergestellt.</p>

    <h2>4. Cookies und Tracking</h2>
    <p>Diese Website setzt keine Cookies und verwendet keine Analyse- oder Tracking-Werkzeuge.</p>

    <h2>5. Externe Links</h2>
    <p>Links zu Google Maps, OpenStreetMap, Tripadvisor, Instagram, TikTok und Facebook werden erst beim Anklicken aufgerufen. Erst dann gelten die Datenschutzbestimmungen des jeweiligen Anbieters.</p>

    <h2>6. Kontaktaufnahme per Telefon oder E-Mail</h2>
    <p>Wenn Sie uns zur Reservierung oder Bestellung kontaktieren, verarbeiten wir Ihre Angaben (z. B. Name, Telefonnummer, Datum, Personenzahl) ausschließlich zur Bearbeitung Ihrer Anfrage (Art. 6 Abs. 1 lit. b DSGVO) und löschen sie, sobald sie nicht mehr benötigt werden.</p>

    <h2>7. Ihre Rechte</h2>
    <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch (Art. 15–21 DSGVO) sowie das Recht auf Beschwerde bei einer Aufsichtsbehörde, in Nordrhein-Westfalen bei der Landesbeauftragten für Datenschutz und Informationsfreiheit NRW.</p>
  </div>
</section>
"""
    page("datenschutz.html", "Datenschutz – Dolce Vita Westerkappeln", "Datenschutzerklärung des Restaurants Dolce Vita in Westerkappeln.", None, body,
         '<meta name="robots" content="noindex">\n')


def notfound_page():
    body = """<section class="page-head" style="border:0;padding-bottom:6rem">
  <div class="wrap">
    <h1>Seite nicht gefunden</h1>
    <p>Diese Seite gibt es leider nicht (mehr). <a href="index.html">Zur Startseite</a> oder direkt zur <a href="speisekarte.html">Speisekarte</a>.</p>
  </div>
</section>
"""
    page("404.html", "Seite nicht gefunden – Dolce Vita Westerkappeln", "Seite nicht gefunden.", None, body,
         '<meta name="robots" content="noindex">\n')


notfound_page(); index_page(); menu_page(); about_page(); reviews_page(); contact_page(); impressum_page(); datenschutz_page()
print("ok")
