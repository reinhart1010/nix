---
layout: page
title: linux/rmdir (Nederlands)
description: "Verwijder directories zonder bestanden."
content_hash: 44c8412759f7b6e61c45f2169f746c002e54a3cc
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/linux/rmdir.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rmdir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rmdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rmdir

Verwijder directories zonder bestanden.
Zie ook: `rm`.
Meer informatie: <https://www.gnu.org/software/coreutils/rmdir>.

- Verwijder specifieke directories:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map1 pad/naar/map2 ...</span>

- Verwijder specifieke geneste directories recursief:

`rmdir --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map1 pad/naar/map2 ...</span>
