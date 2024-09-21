---
layout: page
title: common/renice (Nederlands)
description: "Verander de scheduleringsprioriteit/niceness van lopende processen."
content_hash: bbcc39bc7321dc8c0d3624b2a2d471b63632b1ab
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/renice.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/renice.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/renice.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># renice

Verander de scheduleringsprioriteit/niceness van lopende processen.
Niceness waarden variëren van -20 (meest gunstig voor het proces) tot 19 (minst gunstig voor het proces).
Zie ook: `nice`.
Meer informatie: <https://manned.org/renice>.

- Verhoog/verlaag de prioriteit van een lopend [p]roces:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Verhoog/verlaag de prioriteit van alle processen die eigendom zijn van een [g]ebruiker:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|user</span>

- Verhoog/verlaag de prioriteit van alle processen die behoren tot een proces[g]roep:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_groep</span>
