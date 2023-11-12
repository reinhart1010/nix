---
layout: page
title: common/todoist (română)
description: "Acest program îți permite să folosești Todoist din linia de comandă."
content_hash: e7b576d585d15b8ca6eb51800017f0b16b01f98f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/todoist.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todoist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# todoist

Acest program îți permite să folosești Todoist din linia de comandă.
Mai multe informații: <https://github.com/sachaos/todoist>.

- Adaugă o sarcină:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o_sarcină</span>`"`

- Adaugă o sarcină cu prioritate ridicată cu o etichetă, proiect și dată scadentă:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o_sarcină</span>`" --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --label-ids "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">idul_etichetei</span>`" --project-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numele_proiectului</span>`" --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmr 9am</span>`"`

- Adaugă o sarcină cu prioritate ridicată cu o etichetă, proiect și dată scadentă, folosind modul rapid:

`todoist quick '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numele_proiectului</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmr 9am</span>`" p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o_sarcină</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numele_etichetei</span>`'`

- Enumeră toate sarcinile cu cap de tabel și culori:

`todoist --header --color list`

- Enumeră toate sarcinile cu prioritate ridicată:

`todoist list --filter p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Enumeră toate sarcinile cu prioritate ridicată de astăzi care au eticheta specificată:

`todoist list --filter '(@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numele_etichetei</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>`) & p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`'`
