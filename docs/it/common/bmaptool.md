---
layout: page
title: common/bmaptool (italiano)
description: "Crea o copia blockmap intelligentemente (e quindi più velocemente di `cp` o `dd`)."
content_hash: e4b43a6dc1bb8975e29d7832fc5704abd51ddade
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bmaptool.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bmaptool.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bmaptool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bmaptool

Crea o copia blockmap intelligentemente (e quindi più velocemente di `cp` o `dd`).
Maggiori informazioni: <https://source.tizen.org/documentation/reference/bmaptool>.

- Crea una blockmap da un file immagine:

`bmaptool create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente.img</span>

- Copia un file immagine su sdb:

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- Copia un file immagine compresso su sdb:

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente.img.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>

- Copia un file immagine su sdb senza utilizzare una blockmap:

`bmaptool copy --nobmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente.img</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>
