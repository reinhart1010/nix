---
layout: page
title: common/transmission-edit (Nederlands)
description: "Wijzig aankondigings URL's van torrentbestanden."
content_hash: 6a9f2ae9273176b7ea149825eeeb9ae7ed8fda7e
last_modified_at: 2023-12-01
related_topics:
  - title: English version
    url: /en/common/transmission-edit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-edit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-edit

Wijzig aankondigings URL's van torrentbestanden.
Bekijk ook: `transmission`.
Meer informatie: <https://manned.org/transmission-edit>.

- Voeg een URL toe aan of verwijder deze uit de aankondigingslijst van een torrent:

`transmission-edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>

- Werk de toegangscode van een tracker bij in een torrentbestand:

`transmission-edit --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oude-toegangscode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe-toegangscode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>
