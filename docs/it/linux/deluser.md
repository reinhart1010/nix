---
layout: page
title: linux/deluser (italiano)
description: "Rimuovi un account utente o un utente da un gruppo."
content_hash: 30ead89fdc7f5e4c912202e9cccbbd2aba355c97
last_modified_at: 2023-11-12
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
Maggiori informazioni: <https://manpages.debian.org/latest/adduser/deluser.html>.

- Rimuovi un utente:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Rimuovi un utente insieme alla sua directory home e raccolta mail:

`deluser -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Rimuovi un utente da un gruppo:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>
