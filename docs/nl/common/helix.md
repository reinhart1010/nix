---
layout: page
title: common/helix (Nederlands)
description: "Helix, een post-moderne tekst bewerker, welke verschillende modi beschikbaar stelt tot verschillende manieren van tekst manipulatie."
content_hash: 0d389e0eb35e1992e26f215dfb5b77dd5284b7fb
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/helix.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/helix.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/helix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/helix.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># helix

Helix, een post-moderne tekst bewerker, welke verschillende modi beschikbaar stelt tot verschillende manieren van tekst manipulatie.
Drukken op `i` begint invoegmodus. `<Esc>` begint normale modus, wat toegang geeft tot de Vim commando's.
Meer informatie: <https://helix-editor.com>.

- Open een bestand:

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open bestanden en toon ze naast elkaar:

`helix --vsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2</span>

- Toon de tutorial om  Helix te leren (of open het binnen Helix door op `<Esc>` te drukken en `:tutor` te typen):

`helix --tutor`

- Pas het Helix thema aan:

`:theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thema_naam</span>

- Opslaan en afsluiten:

`:wq<Enter>`

- Geforceerd afsluiten zonder op te slaan:

`:q!<Enter>`

- Maak de laatste verandering ongedaan:

`u`

- Zoek een patroon in het bestand (druk op `n`/`N` om naar de volgende/vorige overeenkomst te gaan):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`<Enter>`
