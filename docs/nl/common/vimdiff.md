---
layout: page
title: common/vimdiff (Nederlands)
description: "Open twee of meer bestanden in `vim` en toon de verschillen."
content_hash: ecf2080b5da6f579a428f858d26a5371fa8b899c
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/vimdiff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vimdiff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vimdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vimdiff

Open twee of meer bestanden in `vim` en toon de verschillen.
Bekijk ook: `vim`, `vimtutor`, `nvim`.
Meer informatie: <https://www.vim.org>.

- Open twee bestanden en toon de verschillen:

`vimdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Verplaats de cursor naar het scherm links|rechts:

`<Ctrl> + w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|l</span>

- Spring naar het vorige verschil:

`[c`

- Spring naar het volgende verschil:

`]c`

- Kopieer het gemarkeerde verschil van het andere scherm naar het huidige scherm:

`do`

- Kopieer het gemarkeerde verschil van het huidige scherm naar het andere scherm:

`dp`

- Update alle markeringen en folds:

`:diffupdate`

- Schakel de gemarkeerde code fold om:

`za`
