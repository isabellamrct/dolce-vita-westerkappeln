// Dolce Vita Westerkappeln – kleine Helfer, ohne Bibliotheken.

(function () {
  "use strict";

  // Öffnungszeiten – bei Änderungen nur hier und in der Tabelle im HTML anpassen.
  // Index: 0 = Sonntag … 6 = Samstag. Zeiten in Minuten ab Mitternacht.
  var HOURS = {
    0: [[13 * 60, 22 * 60]],
    1: [],
    2: [[12 * 60, 14 * 60 + 30], [17 * 60, 22 * 60]],
    3: [[12 * 60, 14 * 60 + 30], [17 * 60, 22 * 60]],
    4: [[12 * 60, 14 * 60 + 30], [17 * 60, 22 * 60]],
    5: [[12 * 60, 14 * 60 + 30], [17 * 60, 22 * 60]],
    6: [[12 * 60, 14 * 60 + 30], [17 * 60, 22 * 60]]
  };

  function fmt(min) {
    var h = Math.floor(min / 60), m = min % 60;
    return h + ":" + (m < 10 ? "0" : "") + m;
  }

  // Uhrzeit in Westerkappeln (Europe/Berlin), unabhängig vom Gerät des Besuchers.
  function berlinNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-GB", {
        timeZone: "Europe/Berlin", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
      }).formatToParts(new Date());
      var map = {};
      parts.forEach(function (p) { map[p.type] = p.value; });
      var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      return { day: days[map.weekday], min: parseInt(map.hour, 10) % 24 * 60 + parseInt(map.minute, 10) };
    } catch (e) {
      var d = new Date();
      return { day: d.getDay(), min: d.getHours() * 60 + d.getMinutes() };
    }
  }

  function status() {
    var now = berlinNow();
    var today = HOURS[now.day];
    for (var i = 0; i < today.length; i++) {
      if (now.min >= today[i][0] && now.min < today[i][1]) {
        return { open: true, text: "Jetzt geöffnet · bis " + fmt(today[i][1]) + " Uhr", day: now.day };
      }
      if (now.min < today[i][0]) {
        return { open: false, text: "Geschlossen · öffnet heute um " + fmt(today[i][0]) + " Uhr", day: now.day };
      }
    }
    var names = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];
    for (var k = 1; k <= 7; k++) {
      var d = (now.day + k) % 7;
      if (HOURS[d].length) {
        var label = k === 1 ? "morgen" : names[d];
        return { open: false, text: "Geschlossen · öffnet " + label + " um " + fmt(HOURS[d][0][0]) + " Uhr", day: now.day };
      }
    }
    return { open: false, text: "", day: now.day };
  }

  var s = status();
  document.querySelectorAll("[data-status]").forEach(function (el) {
    el.innerHTML = '<span class="status-dot' + (s.open ? " open" : "") + '"></span>' + s.text;
  });
  document.querySelectorAll(".hours tr[data-day]").forEach(function (row) {
    if (row.getAttribute("data-day").split(",").indexOf(String(s.day)) > -1) row.classList.add("today");
  });

  // Mobile Navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Schließen" : "Menü";
    });
  }

  // Speisekarte: aktive Rubrik in der Seitennavigation markieren
  var links = document.querySelectorAll(".menu-nav a");
  if (links.length && "IntersectionObserver" in window) {
    var byId = {};
    links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && byId[e.target.id]) {
          links.forEach(function (a) { a.classList.remove("active"); });
          var a = byId[e.target.id];
          a.classList.add("active");
          if (a.scrollIntoView && window.innerWidth <= 860) {
            a.parentNode.parentNode.scrollLeft = a.offsetLeft - 16;
          }
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    document.querySelectorAll(".menu-section").forEach(function (sec) { io.observe(sec); });
  }

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
