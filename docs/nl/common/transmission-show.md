---
layout: page
title: common/transmission-show (Nederlands)
description: "Verkrijg informatie over een torrent bestand"
content_hash: 46d8f666a5565e32c13c8c6ff6562bcf1b75e50e
last_modified_at: 2023-12-01
related_topics:
  - title: English version
    url: /en/common/transmission-show.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-show

Verkrijg informatie over een torrent bestand
Bekijk ook: `transmission`.
Meer informatie: <https://manned.org/transmission-show>.

- Toon metadata voor een specifieke torrent:

`transmission-show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>

- Genereer een magnet-link voor een specifieke torrent:

`transmission-show --magnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>

- Vraag de trackers van een torrent op en toon het huidige aantal peers:

`transmission-show --scrape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>
