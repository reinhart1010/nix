---
layout: page
title: linux/xbps-remove (Nederlands)
description: "XBPS hulpprogramma voor het verwijderen van pakketten."
content_hash: ca95538a30a68d614acc1f04d9a92841e49153de
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/xbps-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbps-remove

XBPS hulpprogramma voor het verwijderen van pakketten.
Bekijk ook: `xbps`.
Meer informatie: <https://manned.org/xbps-remove.1>.

- Verwijder een pakket:

`xbps-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder een pakket en zijn afhankelijkheden:

`xbps-remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijder verweesde pakketten (geïnstalleerd als afhankelijkheden, maar niet langer vereist door een pakket):

`xbps-remove --remove-orphans`

- Verwijder verouderde pakketten van de cache:

`xbps-remove --clean-cache`
