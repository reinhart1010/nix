---
layout: page
title: linux/dmesg (Nederlands)
description: "Schrijf de kernelberichten naar `stdout`."
content_hash: caddcc2a6b1e58c095fb0fd954367776f5f1e5a5
last_modified_at: 2024-09-30
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Schrijf de kernelberichten naar `stdout`.
Meer informatie: <https://manned.org/dmesg>.

- Toon kernelberichten:

`sudo dmesg`

- Toon kernel foutmeldingen:

`sudo dmesg --level err`

- Toon kernelberichten en blijf nieuwe lezen, vergelijkbaar met `tail -f` (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg -w`

- Toon hoeveel fysiek geheugen beschikbaar is op dit systeem:

`sudo dmesg | grep -i memory`

- Toon kernelberichten 1 pagina per keer:

`sudo dmesg | less`

- Toon kernelberichten met een tijdstempel (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg -T`

- Toon kernelberichten in een leesbare vorm (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg -H`

- Kleur output (beschikbaar in kernels 3.5.0 en nieuwer):

`sudo dmesg -L`
