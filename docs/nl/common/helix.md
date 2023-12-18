---
layout: page
title: common/helix (Nederlands)
description: "Helix, een post-moderne tekst bewerker, welke verschillende modi beschikbaar stelt tot verschillende manieren van tekst manipulatie."
content_hash: 2554ef219756ffd9e0762bcdacc435723fcb1e19
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/helix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# helix

Helix, een post-moderne tekst bewerker, welke verschillende modi beschikbaar stelt tot verschillende manieren van tekst manipulatie.
Drukken op `i` begint invoegmodus. `<Esc>` begint normale modus, wat toegang geeft tot de Vim commando's.
Meer informatie: <https://helix-editor.com>.

- Open een bestand:

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

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

- Formateer het bestand:

`:format`
