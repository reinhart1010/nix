---
layout: page
title: common/rc (Nederlands)
description: "Een moderne simplistische poort luisteraar en omgekeerde shell."
content_hash: ada1aec35a4f6f3001fb50d0c42ffdf468d942cf
last_modified_at: 2023-12-22
related_topics:
  - title: English version
    url: /en/common/rc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rc

Een moderne simplistische poort luisteraar en omgekeerde shell.
Vergelijkbaar met `nc`.
Meer informatie: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Start met luisteren op een specifieke poort:

`rc -lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Start een omgekeerde shell:

`rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>
