---
layout: page
title: common/dd (italiano)
description: "Converti e copia un file."
content_hash: ff1eca4546c909bdaeb24f0ba6fb2522a0ee0b3c
last_modified_at: 2024-06-11
related_topics:
  - title: Deutsch version
    url: /de/common/dd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dd

Converti e copia un file.
Maggiori informazioni: <https://manned.org/man/dd.1p>.

- Crea un disco USB avviabile da un file ISO e mostra il progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco_usb</span>` status=progress`

- Clona un disco in un altro a blocchi di 4MB, ignora gli errori e mostra il progresso:

`dd bs=4M conv=noerror status=progress if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco_sorgente</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco_destinazione</span>

- Genera un file di 100 byte randomici utilizzando il driver random del kernel:

`dd bs=100 count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_random</span>

- Testa la performance in scrittura di un disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_1GB</span>
