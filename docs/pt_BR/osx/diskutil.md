---
layout: page
title: osx/diskutil (português (Brasil))
description: "Utilitário para gerenciar discos e volumes locais."
content_hash: bf0a4a49de61418cd4a155a00c97765ac6bb66e3
related_topics:
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diskutil

Utilitário para gerenciar discos e volumes locais.
Mais informações: <https://ss64.com/osx/diskutil.html>.

- Lista todos os discos, partições, e volumes montados atualmente disponíveis:

`diskutil list`

- Repara as estruturas de dados do sistema de arquivos de um volume:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Desmonta um volume:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Ejeta um CD/DVD (desmonta primeiro):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
