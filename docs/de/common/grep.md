---
layout: page
title: common/grep (Deutsch)
description: "Findet Ausdrücke in einem Eingabetext."
content_hash: ccda58b3309be9038a765653173caa80b0ca0812
last_modified_at: 2023-11-12
related_topics:
  - title: dansk version
    url: /da/common/grep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/grep.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/grep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/grep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/grep.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/grep.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grep

Findet Ausdrücke in einem Eingabetext.
Unterstützt einfache Muster und reguläre Ausdrücke.
Weitere Informationen: <https://www.gnu.org/software/grep/manual/grep.html>.

- Suche nach einem Ausdruck in einer Datei:

`grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Suche nach einem exakten Ausdruck:

`grep -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exakter_ausdruck</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Suche nach Ausdrücken [R]ekursiv im aktuellen Verzeichnis, zeige zugehörige Zeilen[n]ummern und [I]gnoriere Binärdateien:

`grep -RIn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>` .`

- Benutze erweiterte reguläre Ausdrücke (unterstützt `?`, `+`, `{}`, `()` und `|`) ohne Beachtung der Groß-, Kleinschreibung:

`grep -Ei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Zeige 3 Zeilen Kontext um [C], vor [B] oder nach [A] jedem Ergebnis:

`grep -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C|B|A</span>` 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib den Dateinamen mit zugehöriger Zeilennummer für jedes Ergebnis aus:

`grep -Hn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Benutze STDIN, anstatt einer Datei:

`echo "input" | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>

- In[v]ertiere das Ergebnis um bestimmte Ausdrücke auszuschließen:

`grep -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ausdruck</span>
