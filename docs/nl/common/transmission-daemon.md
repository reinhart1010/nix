---
layout: page
title: common/transmission-daemon (Nederlands)
description: "Daemon bediend met `transmission-remote` of de webinterface."
content_hash: a75511b320ef311af54894396c7140818e4926ab
last_modified_at: 2023-12-01
related_topics:
  - title: English version
    url: /en/common/transmission-daemon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-daemon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-daemon

Daemon bediend met `transmission-remote` of de webinterface.
Bekijk ook: `transmission`.
Meer informatie: <https://manned.org/transmission-daemon>.

- Start een headless `transmission` sessie:

`transmission-daemon`

- Start en bewaak een specifieke map voor nieuwe torrents:

`transmission-daemon --watch-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Dump daemon-instellingen in JSON formaat:

`transmission-daemon --dump-settings > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.json</span>

- Start met specifieke instellingen voor de web interface:

`transmission-daemon --auth --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9091</span>` --allowed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>
