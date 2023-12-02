---
layout: page
title: common/transmission-daemon (Nederlands)
description: "Daemon bediend met `transmission-remote` of de webinterface."
content_hash: a75511b320ef311af54894396c7140818e4926ab
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/common/transmission-daemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-daemon

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
