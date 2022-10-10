---
layout: page
title: common/ping (Deutsch)
description: "Sendet ICMP ECHO_REQUEST Pakete an andere Geräte im Netzwerk."
content_hash: d2a1a64ba6d703a4a6d5fb7ebe40a92380944e25
related_topics:
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ping

Sendet ICMP ECHO_REQUEST Pakete an andere Geräte im Netzwerk.
Weitere Informationen: <https://manned.org/ping>.

- Sende Pings an ein Gerät im Netzwerk:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende nur eine bestimmte Anzahl an Pings:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende Pings und bestimme das Interval in Sekunden zwischen diesen (standardmäßig ist es eine Sekunde):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekunden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende Pings ohne symbolische Namen nach Adressen aufzulösen:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende Pings und signalisiere eine erfolgreiche Antwort durch ein Bell Signal (wenn das Terminal es unterstützt):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Zeige auch eine Nachricht, wenn keine Antwort empfangen wurde:

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>
