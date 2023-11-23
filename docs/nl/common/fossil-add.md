---
layout: page
title: common/fossil-add (Nederlands)
description: "Plaats bestanden of mappen in Fossil versiebeheer."
content_hash: 1aaa3eec5a187a93dcc0bec84c4f364963b3d93b
last_modified_at: 2023-11-23
related_topics:
  - title: English version
    url: /en/common/fossil-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fossil-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fossil add

Plaats bestanden of mappen in Fossil versiebeheer.
Meer informatie: <https://fossil-scm.org/home/help/add>.

- Plaats een bestand of map in versiebeheer, zodat het in de huidige checkout zit:

`fossil add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map_of_bestand</span>

- Verwijder alle toegevoegde bestanden uit de huidige checkout:

`fossil add --reset`
