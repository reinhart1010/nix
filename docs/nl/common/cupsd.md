---
layout: page
title: common/cupsd (Nederlands)
description: "Server daemon voor de CUPS print server."
content_hash: 3afa599d1909ac63a43aa9ec24a5ca5ac3db4e0b
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/cupsd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsd

Server daemon voor de CUPS print server.
Meer informatie: <https://openprinting.github.io/cups/doc/man-cupsd.html>.

- Start `cupsd` op de achterground, aka. als een daemon:

`cupsd`

- Start `cupsd` op de voorgrond:

`cupsd -f`

- Draai `cupsd` op aanvraag (vaak gebruikt door `launchd` of `systemd`):

`cupsd -l`

- Start `cupsd` met het gespecificeerde [`c`]`upsd.conf` configuratie bestand:

`cupsd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/cupsd.conf</span>

- Start `cupsd` met het gespecificeerde `cups-bestanden.conf` configuratie bestand:

`cupsd -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/cups-bestanden.conf</span>

- [t]est het [`c`]`upsd.conf` configuratie bestand voor fouten:

`cupsd -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/cupsd.conf</span>

- [t]est het `cups-bestanden.conf` configuratie bestand voor fouten:

`cupsd -t -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/cups-bestanden.conf</span>

- Toon alle beschikbare opties:

`cupsd -h`
