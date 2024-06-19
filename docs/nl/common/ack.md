---
layout: page
title: common/ack (Nederlands)
description: "Een zoektool zoals grep, geoptimaliseerd voor ontwikkelaars."
content_hash: b567132b1cf17b8e7f0520f6ed1599cd08b596e9
last_modified_at: 2024-06-19
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

Een zoektool zoals grep, geoptimaliseerd voor ontwikkelaars.
Bekijk ook: `rg`, dat is veel sneller.
Meer informatie: <https://beyondgrep.com/documentation>.

- Zoek recursief naar bestanden met een tekenreeks of reguliere expressie in de huidige map:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek naar een niet-hoofdlettergevoelig patroon:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek naar lijnen die overeenkomen met een patroon en druk alleen de overeenkomende tekst af en niet de rest van de lijn:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Beperk het zoeken tot bestanden van een specifiek type:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Zoek niet in bestanden van een specifiek type:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Tel het totaal aantal gevonden matches:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Toon alleen voor elk bestand de bestandsnamen en het aantal overeenkomsten:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekpatroon</span>`"`

- Maak een lijst van alle waarden die kunnen worden gebruikt met `--type`:

`ack --help-types`
