---
layout: page
title: linux/update-alternatives (Nederlands)
description: "Een handig hulpmiddel voor het onderhouden van symbolische links om standaard commando's te bepalen."
content_hash: 56e13bfe7966c76006b40ae40a4f3c78c28b7b3a
last_modified_at: 2023-11-18
related_topics:
  - title: English version
    url: /en/linux/update-alternatives.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/update-alternatives.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># update-alternatives

Een handig hulpmiddel voor het onderhouden van symbolische links om standaard commando's te bepalen.
Meer informatie: <https://manned.org/update-alternatives>.

- Voeg een symbolische link toe:

`sudo update-alternatives --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/symlink</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/commando_binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">priority</span>

- Configureer een symbolische link voor `java`:

`sudo update-alternatives --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- Verwijder een symbolische link:

`sudo update-alternatives --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/opt/java/jdk1.8.0_102/bin/java</span>

- Toon informatie over een specifiek commando:

`update-alternatives --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- Toon alle commando's en hun huidige selectie:

`update-alternatives --get-selections`
