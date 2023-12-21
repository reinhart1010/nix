---
layout: page
title: linux/resolvectl (Nederlands)
description: "Resolve domeinnamen, IPv4 en IPv6 adressen, DNS resource records en services."
content_hash: ee82769adb7c2bd7f2e0adc94b53779c3487f183
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/linux/resolvectl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/resolvectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/resolvectl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/resolvectl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># resolvectl

Resolve domeinnamen, IPv4 en IPv6 adressen, DNS resource records en services.
Bekijk en herconfigureer de DNS resolver.
Meer informatie: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Toon DNS instellingen:

`resolvectl status`

- Resolve de IPv4 en IPv6 adressen voor een of meerdere domeinen:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein1 domein2 ...</span>

- Verkrijg het domein van een gespecificeerd IP adres:

`resolvectl query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>

- Flush alle lokale DNS caches:

`resolvectl flush-caches`

- Toon DNS statistieken (transacties, cache en DNSSEC oordelen):

`resolvectl statistics`

- Verkrijg een MX record van een domein:

`resolvectl --legend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">no</span>` --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MX</span>` query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>

- Resolve een SRV record, bijvoorbeeld _xmpp-server._tcp gmail.com:

`resolvectl service _`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>`._`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam</span>

- Verkrijg een TLS sleutel:

`resolvectl tlsa tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>`:443`
