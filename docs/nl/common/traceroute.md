---
layout: page
title: common/traceroute (Nederlands)
description: "Toon het pad dat pakketjes volgen naar een netwerkhost."
content_hash: 0abb4b6a3cba398c2b0de1fc3b8b1a49bccf4c52
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/traceroute.html
    icon: bi bi-globe
tldri18n_status: 2
---
# traceroute

Toon het pad dat pakketjes volgen naar een netwerkhost.
Meer informatie: <https://manned.org/traceroute>.

- Traceroute naar een host:

`traceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Schakel IP-adres en hostnaam mapping uit:

`traceroute -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Specificeer wachttijd in seconden voor antwoord:

`traceroute --wait=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Specificeer het aantal queries per hop:

`traceroute --queries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Specificeer de grootte in bytes van het peilpakket:

`traceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Bepaal de MTU naar de bestemming:

`traceroute --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Gebruik ICMP in plaats van UDP voor tracerouting:

`traceroute --icmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
