---
layout: page
title: common/cupsd (Nederlands)
description: "Server daemon voor de CUPS print server."
content_hash: 97bbc81c05ee9bd676e0aa227e62dc80535fb460
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/cupsd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsd

Server daemon voor de CUPS print server.
Meer informatie: <https://www.cups.org/doc/man-cupsd.html>.

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
