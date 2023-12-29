---
layout: page
title: common/lp (Nederlands)
description: "Print bestanden."
content_hash: 66401793bc13e08f85133db76ffb5295989f39b7
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/lp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lp

Print bestanden.
Meer informatie: <https://manned.org/lp>.

- Print de output van een commando met de standaard printer (bekijk het `lpstat` commando):

`echo "test" | lp`

- Print een bestand met de standaard printer:

`lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestandsnaam</span>

- Print een bestand met een printer met naam (bekijk het `lpstat` commando):

`lp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestandsnaam</span>

- Print N kopieën van een bestand met de standaard printer (vervang N met het gewenste aantal kopieën):

`lp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestandsnaam</span>

- Print alleen specifieke pagina's met de standaard printer (print pagina's 1, 3-5, and 16):

`lp -P 1,3-5,16 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestandsnaam</span>

- Hervat het printen van een taak:

`lp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>` -H resume`
