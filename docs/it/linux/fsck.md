---
layout: page
title: linux/fsck (italiano)
description: "Controlla l'integrità di un filesystem o lo ripara. Il filesystem non dev'essere montato al momento in cui il comando viene eseguito."
content_hash: 4b0997f977b8ef3327372c817e1ead15b3e58da8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

Controlla l'integrità di un filesystem o lo ripara. Il filesystem non dev'essere montato al momento in cui il comando viene eseguito.
Maggiori informazioni: <https://manned.org/fsck>.

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati:

`fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati e per ognuno consente all'utente di scegliere interattivamente se ripararlo:

`fsck -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati e riparandoli automaticamente:

`fsck -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
