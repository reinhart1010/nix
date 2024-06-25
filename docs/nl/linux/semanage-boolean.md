---
layout: page
title: linux/semanage-boolean (Nederlands)
description: "Beheer persistente SELinux-boolean-instellingen."
content_hash: 7ea58a3e276a46b322238f87123222a47672b38e
last_modified_at: 2024-06-25
related_topics:
  - title: English version
    url: /en/linux/semanage-boolean.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/semanage-boolean.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># semanage boolean

Beheer persistente SELinux-boolean-instellingen.
Zie ook: `semanage` voor het beheren van SELinux-beleid, `getsebool` voor het controleren van boolean-waarden, en `setsebool` voor het toepassen van niet-blijvende boolean-instellingen.
Meer informatie: <https://manned.org/man/semanage-boolean>.

- Toon alle boolean-instellingen:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Toon alle door de gebruiker gedefinieerde boolean-instellingen zonder koppen:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-C|--locallist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--noheading</span>

- Stel een boolean blijvend in of uit:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>
