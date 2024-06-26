---
layout: page
title: common/whois (Nederlands)
description: "Opdrachtregelclient voor het WHOIS (RFC 3912) protocol."
content_hash: 9ea2706398217dfb91f4370e2902d9c80a754556
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/common/whois.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whois.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/whois.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whois

Opdrachtregelclient voor het WHOIS (RFC 3912) protocol.
Meer informatie: <https://github.com/rfc1036/whois>.

- Verkrijg informatie over een domeinnaam:

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Verkrijg informatie over een IP-adres:

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Verkrijg het contact om misbruik te melden voor een IP-adres:

`whois -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>
