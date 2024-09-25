---
layout: page
title: linux/xbps-query (Nederlands)
description: "XBPS hulpprogramma om te zoeken naar een pakket en repository informatie."
content_hash: af6b71cb32292cac42532d8d840e3f781c0b1da8
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/xbps-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbps-query

XBPS hulpprogramma om te zoeken naar een pakket en repository informatie.
Bekijk ook: `xbps`.
Meer informatie: <https://manned.org/xbps-query.1>.

- Zoek naar een pakket in externe repositories met behulp van een reguliere expressie of een trefwoord (als `--regex` wordt weggelaten):

`xbps-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie|trefwoord</span>` --repository --regex`

- Toon informatie over een geïnstalleerd pakket:

`xbps-query --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon informatie over een pakket in externe repositories:

`xbps-query --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>` --repository`

- Toon alle geregistreerde pakketen in de pakket database:

`xbps-query --list-pkgs`

- Toon expliciet geïnstalleerde pakketen (bijv. niet automatisch geïnstalleerd als afhankelijkheden):

`xbps-query --list-manual-pkgs`
