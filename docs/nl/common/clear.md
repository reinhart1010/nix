---
layout: page
title: common/clear (Nederlands)
description: "Leegt het scherm van de terminal."
content_hash: d8bfd89e5c5aebd87dca15eecbc02cc0ddd40c9c
last_modified_at: 2024-08-13
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clear

Leegt het scherm van de terminal.
Meer informatie: <https://manned.org/clear>.

- Maak het scherm leeg (gelijk aan het indrukken van Control-L in de Bash-shell):

`clear`

- Maak het scherm leeg maar behoud de scrollbackbuffer van de terminal:

`clear -x`

- Geef het type terminal aan dat leeggemaakt moet worden (standaard ingesteld op de waarde van de omgevingsvariabele `TERM`):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_of_terminal</span>

- Toon de versie van `ncurses` die door `clear` wordt gebruikt:

`clear -V`
