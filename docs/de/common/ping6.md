---
layout: page
title: common/ping6 (Deutsch)
description: "Sendet ICMP ECHO_REQUEST Pakete an andere Geräte im Netzwerk, welche mittels IPv6-Adressen identifiziert werden."
content_hash: cf343d4378ca55d970bbeb73e355908372e250f4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ping6.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping6.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping6

Sendet ICMP ECHO_REQUEST Pakete an andere Geräte im Netzwerk, welche mittels IPv6-Adressen identifiziert werden.
Weitere Informationen: <https://manned.org/ping6>.

- Sende Pings an ein Gerät im Netzwerk:

`ping6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende nur eine bestimmte Anzahl an Pings:

`ping6 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anzahl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende Pings und bestimme das Interval in Sekunden zwischen diesen (standardmäßig ist es eine Sekunde):

`ping6 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sekunden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende Pings ohne symbolische Namen nach Adressen aufzulösen:

`ping6 -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Sende Pings und signalisiere eine erfolgreiche Antwort durch ein Bell Signal (wenn das Terminal es unterstützt):

`ping6 -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>
