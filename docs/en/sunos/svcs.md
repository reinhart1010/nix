---
layout: page
title: sunos/svcs (English)
description: "List information about running services."
content_hash: ebabb92f0d57783324d15ecbd0ecf4b9e47017d9
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/sunos/svcs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcs.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcs

List information about running services.
More information: <https://www.unix.com/man-page/linux/1/svcs>.

- List all running services:

`svcs`

- List services that are not running:

`svcs -vx`

- List information about a service:

`svcs apache`

- Show location of service log file:

`svcs -L apache`

- Display end of a service log file:

`tail $(svcs -L apache)`
