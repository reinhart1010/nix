---
layout: page
title: common/for (Nederlands)
description: "Voer een commando meerdere keren uit."
content_hash: 67d5c957eb136a41cf61bfca4ec22075be93440e
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/common/for.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/for.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># for

Voer een commando meerdere keren uit.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- Voer de gegeven commando's uit voor elk van de opgegeven items:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item1 item2 ...</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop wordt uitgevoerd"</span>`; done`

- Itereer over een gegeven reeks nummers:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{van</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tot</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stap}</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop wordt uitgevoerd"</span>`; done`

- Itereer over een gegeven lijst van bestanden:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop wordt uitgevoerd"</span>`; done`

- Itereer over een gegeven lijst van directories:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory1/ pad/naar/directory2/ ...</span>`; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop wordt uitgevoerd"</span>`; done`

- Voer een gegeven commando uit in elke directory:

`for `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in */; do (cd "$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`" || continue; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Loop wordt uitgevoerd"</span>`) done`
