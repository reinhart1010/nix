---
layout: page
title: common/dd (italiano)
description: "Converti e copia un file."
content_hash: 0f667815e7b461828a9e0c0ba99870ea98b8ae7c
related_topics:
  - title: Deutsch version
    url: /de/common/dd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dd.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dd

Converti e copia un file.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/dd>.

- Crea un disco USB avviabile da un file ISO e mostra il progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disco_usb</span>` status=progress`

- Clona un disco in un altro a blocchi di 4MB, ignora gli errori e mostra il progresso:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disco_sorgente</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disco_destinazione</span>` bs=4M conv=noerror status=progress`

- Genera un file di 100 byte randomici utilizzando il driver random del kernel:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_random</span>` bs=100 count=1`

- Testa la performance in scrittura di un disco:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1GB</span>` bs=1024 count=1000000`

- Mostra il progresso di un'operazione dd in corso (comando da eseguire in un'altra shell):

`kill -USR1 $(pgrep ^dd)`
