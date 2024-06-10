---
layout: page
title: common/dd (Nederlands)
description: "Converteer en kopieer een bestand."
content_hash: 40b2a0085c549e1bd09cbee8d53b13e0ed530f79
last_modified_at: 2024-06-10
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
  - title: italiano version
    url: /it/common/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Converteer en kopieer een bestand.
Meer informatie: <https://manned.org/man/dd.1p>.

- Maak een opstartbare USB-schijf van een isohybrid-bestand (zoals `archlinux-xxx.iso`):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb_schijf</span>

- Kopieer een schijf naar een andere schijf met een blokgrootte van 4 MiB en schrijf alle gegevens voordat het commando eindigt:

`dd bs=4194304 conv=fsync if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron_schijf</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel_schijf</span>

- Genereer een bestand met een specifiek aantal willekeurige bytes met behulp van de kernel random driver:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/willekeurig_bestand</span>

- Benchmark de sequentiële schrijfsnelheid van een schijf:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_1GB</span>

- Maak een systeemback-up en sla deze op in een IMG bestand (kan later worden hersteld door `if` en `of` om te wisselen):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/schijf_apparaat</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.img</span>
