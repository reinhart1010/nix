---
layout: page
title: common/xzless (Nederlands)
description: "Tekst weergeven van `xz` en `lzma` gecomprimeerde bestanden."
content_hash: 88dd6ca50debb97e50e132c9bebd2a45c2a9c41b
last_modified_at: 2023-11-25
related_topics:
  - title: English version
    url: /en/common/xzless.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzless.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzless

Tekst weergeven van `xz` en `lzma` gecomprimeerde bestanden.
Zie ook: `less`.
Meer informatie: <https://manned.org/xzless>.

- Bekijk een gecomprimeerd bestand:

`xzless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bekijk een gecomprimeerd bestand en toon regelnummers:

`xzless --LINE-NUMBERS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bekijk een gecomprimeerd bestand en stop als het hele bestand op het eerste scherm kan worden weergegeven:

`xzless --quit-if-one-screen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
