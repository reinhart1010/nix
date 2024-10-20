---
layout: page
title: linux/eselect-locale (Nederlands)
description: "Een `eselect`-module voor het beheren van de `LANG`-omgevingsvariabele, die de systeemtaal instelt."
content_hash: 97392fd8f382eaa412fffae069e42556bfb5bea8
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/eselect-locale.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eselect locale

Een `eselect`-module voor het beheren van de `LANG`-omgevingsvariabele, die de systeemtaal instelt.
Meer informatie: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- Toon van beschikbare locales:

`eselect locale list`

- Stel de `LANG`-omgevingsvariabele in `/etc/profile.env` in op naam of index van de `list`-opdracht:

`eselect locale set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam|index</span>

- Toon de waarde van `LANG` in `/etc/profile.env`:

`eselect locale show`
