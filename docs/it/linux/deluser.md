---
layout: page
title: linux/deluser (italiano)
description: "Rimuovi un account utente o un utente da un gruppo."
content_hash: ee5264e020d67e173367a7f436ac12d00ef716b4
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/deluser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/deluser.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/deluser.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># deluser

Rimuovi un account utente o un utente da un gruppo.
Maggiori informazioni: <https://manned.org/deluser>.

- Rimuovi un utente:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Rimuovi un utente insieme alla sua directory home e raccolta mail:

`deluser -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Rimuovi un utente da un gruppo:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>
