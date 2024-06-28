---
layout: page
title: common/traceroute (Nederlands)
description: "Toon het pad dat pakketjes volgen naar een netwerkhost."
content_hash: 0abb4b6a3cba398c2b0de1fc3b8b1a49bccf4c52
last_modified_at: 2024-06-28
related_topics:
  - title: English version
    url: /en/common/traceroute.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/traceroute.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># traceroute

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
