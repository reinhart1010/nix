---
layout: page
title: linux/mycli (Nederlands)
description: "Een CLI voor MySQL, MariaDB en Percona met automatische aanvulling en syntaxisaccentuering."
content_hash: 4ea3c12634f87371d728bb4846c153e6594e90c1
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/linux/mycli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mycli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mycli

Een CLI voor MySQL, MariaDB en Percona met automatische aanvulling en syntaxisaccentuering.
Meer informatie: <https://manned.org/mycli>.

- Verbinden met een database met de huidige ingelogde gebruiker:

`mycli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_naam</span>

- Verbinden met een database met de opgegeven gebruiker:

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_naam</span>

- Verbinden met een database op de opgegeven host met de opgegeven gebruiker:

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_naam</span>
