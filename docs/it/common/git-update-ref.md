---
layout: page
title: common/git-update-ref (italiano)
description: "Crea, aggiorna e cancella riferimenti Git."
content_hash: 9ac7c85ed23eed80ca004f9e3dd49ac703909e92
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-update-ref.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-update-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-ref.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git update-ref

Crea, aggiorna e cancella riferimenti Git.
Maggiori informazioni: <https://git-scm.com/docs/git-update-ref>.

- Cancella un riferimento, utile per resettare il primo commit in modo soft:

`git update-ref -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Aggiorna un riferimento con un messaggio:

`git update-ref -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4e95e05</span>
