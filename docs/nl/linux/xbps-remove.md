---
layout: page
title: linux/xbps-remove (Nederlands)
description: "XBPS hulpprogramma voor het verwijderen van pakketten."
content_hash: f52297c01d4a2b9c8ecc31a29e62890e529c6be4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xbps-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbps-remove

XBPS hulpprogramma voor het verwijderen van pakketten.
Bekijk ook: `xbps`.
Meer informatie: <https://man.voidlinux.org/xbps-remove.1>.

- Verwijder een pakket:

`xbps-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder een pakket en zijn afhankelijkheden:

`xbps-remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder verweesde pakketten (geïnstalleerd als afhankelijkheden, maar niet langer vereist door een pakket):

`xbps-remove --remove-orphans`

- Verwijder verouderde pakketten van de cache:

`xbps-remove --clean-cache`
