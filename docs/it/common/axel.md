---
layout: page
title: common/axel (italiano)
description: "Downloader accelerato."
content_hash: 8682e741c1d2f403a6c738a6ea98f2adb813b89b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/axel.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/axel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/axel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/axel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/axel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/axel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# axel

Downloader accelerato.
Supporta HTTP, HTTPS e FTP.
Maggiori informazioni: <https://github.com/axel-download-accelerator/axel>.

- Scarica un file da un URL:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Scarica specificando il nome del file da creare:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Scarica sfruttando connessioni multiple:

`axel -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_connessioni</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Cerca dei mirror:

`axel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_mirror</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limita la velocità di download (in bytes al secondo):

`axel -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">limite_velocità</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
