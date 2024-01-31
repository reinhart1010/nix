---
layout: page
title: osx/diskutil (português (Brasil))
description: "Utilitário para gerenciar discos e volumes locais."
content_hash: 42a429ee4350366bee38a34da5667429cdc212ce
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/diskutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil

Utilitário para gerenciar discos e volumes locais.
Mais informações: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Lista todos os discos, partições, e volumes montados atualmente disponíveis:

`diskutil list`

- Repara as estruturas de dados do sistema de arquivos de um volume:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Desmonta um volume:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Ejeta um CD/DVD (desmonta primeiro):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
