---
layout: page
title: common/pio-package (Nederlands)
description: "Beheer pakketten in het register."
content_hash: 57c2b9d444204c7b9de0da76a0298c98b74a574f
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-package.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio package

Beheer pakketten in het register.
Pakketten kunnen alleen verwijderd worden binnen 72 uur (3 dagen) vanaf de datum dat ze gepubliceerd zijn.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/package/>.

- Maak een pakket tarball van de huidige map:

`pio package pack --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.tar.gz</span>

- Maak en publiceer een pakket tarball van de huidige map:

`pio package publish`

- Publiceer de huidige map en beperk de publieke toegang:

`pio package publish --private`

- Publiceer een pakket:

`pio package publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.tar.gz</span>

- Publiceer een pakket met een aangepaste release datum (UTC):

`pio package publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.tar.gz</span>` --released-at "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-04-08 21:15:38</span>`"`

- Verwijder alle versies van een gepubliceerd pakket van het register:

`pio package unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder een specifieke versie van een gepubliceerd pakket van het register:

`pio package unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Maak de verwijdering ongedaan en zet alle versies of een specifieke versie van het pakket terug in het register:

`pio package unpublish --undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
