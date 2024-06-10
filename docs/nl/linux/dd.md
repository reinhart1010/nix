---
layout: page
title: linux/dd (Nederlands)
description: "Converteer en kopieer een bestand."
content_hash: 41bde07a2cc7f63b82f17dd9c972cfca59830190
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/linux/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Converteer en kopieer een bestand.
Meer informatie: <https://www.gnu.org/software/coreutils/dd>.

- Maak een opstartbare USB-schijf van een isohybrid-bestand (zoals `archlinux-xxx.iso`) en toon de voortgang:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_schijf</span>` status=progress`

- Kopieer een schijf naar een andere schijf met een blokgrootte van 4 MiB en schrijf alle gegevens voordat het commando eindigt:

`dd bs=4M conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/bron_schijf</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/doel_schijf</span>

- Genereer een bestand met een specifiek aantal willekeurige bytes met behulp van de kernel random driver:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/willekeurig_bestand</span>

- Benchmark de sequentiële schrijfsnelheid van een schijf:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_1GB</span>

- Maak een systeemback-up, sla deze op in een IMG bestand (kan later worden hersteld door `if` en `of` om te wisselen) en toon de voortgang:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/schijf_apparaat</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.img</span>` status=progress`

- Bekijk de voortgang van een lopende `dd` operatie (voer dit commando uit vanaf een andere shell):

`kill -USR1 $(pgrep -x dd)`
