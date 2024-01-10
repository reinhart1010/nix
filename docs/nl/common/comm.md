---
layout: page
title: common/comm (Nederlands)
description: "Toon overeenkomstige regels tussen twee bestanden. Beide bestanden dienen gesorteerd te zijn."
content_hash: ee4a5fb9ef4115293843784ab2925df2bf2981f7
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/comm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/comm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/comm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comm

Toon overeenkomstige regels tussen twee bestanden. Beide bestanden dienen gesorteerd te zijn.
Meer informatie: <https://www.gnu.org/software/coreutils/comm>.

- Produceer drie tab-gescheiden kolommen: regels die alleen voorkomen in het eerste bestand, regels die alleen voorkomen in het tweede bestand en overeenkomstige regels tussen beide bestanden:

`comm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand2</span>

- Toon alleen overeenkomstige regels van beide bestanden:

`comm -12 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand2</span>

- Toon alleen de overeenkomstige regels van beide bestanden en lees een bestand vanaf `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand1</span>` | comm -12 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand2</span>

- Sla regels die alleen in het eerste bestand worden gevonden op in een derde bestand:

`comm -23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alleen_bestand1</span>

- Toon de regels welke alleen in het tweede bestand gevonden worden, als de bestanden niet gesorteerd zijn:

`comm -13 <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand1</span>`) <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand2</span>`)`
