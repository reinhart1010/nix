---
layout: page
title: common/certutil (Nederlands)
description: "Beheer sleutels en certificaten in zowel NSS-databases als andere NSS-tokens."
content_hash: 094918819a46f1544f68e4bd42c5763aca2a1fef
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/certutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

Beheer sleutels en certificaten in zowel NSS-databases als andere NSS-tokens.
Meer informatie: <https://manned.org/certutil>.

- Maak een [N]ieuwe certificaatdatabase aan in de huidige [d]irectory:

`certutil -N -d .`

- Toon alle certificaten in een database:

`certutil -L -d .`

- Toon alle private [S]leutels in een database door het wachtwoord[b]estand te specificeren:

`certutil -K -d . -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/wachtwoord_bestand.txt</span>

- [V]oeg het ondertekende certificaat toe aan de database van de aanvrager door een [b]ijnaam, [v]ertrouwensattributen en een [i]nvoer-CRT-bestand te specificeren:

`certutil -A -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_certificaat</span>`" -t ",," -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.crt</span>` -d .`

- Voeg subject alternative names toe aan een [c]ertificaat met een specifieke sleutelgrootte ([g]):

`certutil -S -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/wachtwoordbestand.txt</span>` -d . -t ",," -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_certificaat</span>`" -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_naam</span>`" -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -s "CN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">common_name</span>`,O=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatie</span>`"`
