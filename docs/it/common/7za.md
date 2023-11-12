---
layout: page
title: common/7za (italiano)
description: "Archiviatore di file con alto fattore di compressione."
content_hash: 1242dda9594671d0e828973f66fbebe76f4f9b42
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/7za.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7za.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7za.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7za.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7za.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7za.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/7za.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7za.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7za.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7za.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7za.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7za.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7za.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7za.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># 7za

Archiviatore di file con alto fattore di compressione.
Versione standalone di `7z` con supporto a meno tipi di archivi.
Maggiori informazioni: <https://manned.org/7za>.

- Archivia un file o una directory:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Estrai un archivio mantenendo la gerarchia delle directory:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.7z</span>

- Archivia utilizzando uno specifico tipo di archivio:

`7za a -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zip|gzip|bzip2|tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Elenca i tipi di archivio supportati:

`7za i`

- Elenca i contenuti in un archivio:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivio</span>
