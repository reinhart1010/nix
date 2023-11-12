---
layout: page
title: linux/calcurse (English)
description: "A text-based calendar and scheduling application for the command-line."
content_hash: b626f3f6db7c90935e3a1c33b1c0559cfbae465e
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/calcurse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calcurse

A text-based calendar and scheduling application for the command-line.
More information: <https://calcurse.org>.

- Start `calcurse` on interactive mode:

`calcurse`

- Print the appointments and events for the current day and exit:

`calcurse --appointment`

- Remove all local calcurse items and import remote objects:

`calcurse-caldav --init=keep-remote`

- Remove all remote objects and push local calcurse items:

`calcurse-caldav --init=keep-local`

- Copy local objects to the CalDAV server and vice versa:

`calcurse-caldav --init=two-way`
