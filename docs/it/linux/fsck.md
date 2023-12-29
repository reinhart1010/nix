---
layout: page
title: linux/fsck (italiano)
description: "Controlla l'integrità di un filesystem o lo ripara. Il filesystem non dev'essere montato al momento in cui il comando viene eseguito."
content_hash: cc78bcb7d57dd3a4fa705b6d2863c08988411e2c
last_modified_at: 2023-12-29
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

`sudo fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati e per ognuno consente all'utente di scegliere interattivamente se ripararlo:

`sudo fsck -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati e riparandoli automaticamente:

`sudo fsck -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
