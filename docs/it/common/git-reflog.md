---
layout: page
title: common/git-reflog (italiano)
description: "Mostra la cronologia delle modifiche a riferimenti locali come HEAD, rami o tag."
content_hash: 6f541fa4d3f58dd45d24d5f5290f00799fec573f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-reflog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reflog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reflog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reflog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reflog

Mostra la cronologia delle modifiche a riferimenti locali come HEAD, rami o tag.
Maggiori informazioni: <https://git-scm.com/docs/git-reflog>.

- Mostra il reflog di HEAD:

`git reflog`

- Mostra il reflog di uno specifico ramo:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Mostra le ultime 5 voci del reflog:

`git reflog -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
