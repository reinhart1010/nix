---
layout: page
title: common/dd (italiano)
description: "Converti e copia un file."
content_hash: 59ca648928ca0970981e0cec424204b71308a8bd
last_modified_at: 2024-06-15
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
tldri18n_status: 2
---
# dd

Converti e copia un file.
Maggiori informazioni: <https://manned.org/dd.1p>.

- Crea un disco USB avviabile da un file ISO e mostra il progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco_usb</span>` status=progress`

- Clona un disco su un altro disco a blocchi con grandezza di 4 MiB e scarica le scritture prima che il comando termini:

`dd bs=4194304 conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco_sorgente</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco_destinazione</span>

- Genera un file con un numero specifico di byte randomici utilizzando il driver random del kernel:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_random</span>

- Testa la performance in scrittura di un disco:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_1GB</span>

- Crea un backup di sistema, salvalo in un file IMG (può essere ripristinato in seguito scambiando `if` e `of`), e mostra il progresso:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disco</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.img</span>` status=progress`
