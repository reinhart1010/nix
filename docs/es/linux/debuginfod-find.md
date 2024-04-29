---
layout: page
title: linux/debuginfod-find (español)
description: "Solicita datos relacionados con debuginfo."
content_hash: 5ae2753936cede588b8014eff72b26e0e5d0a061
last_modified_at: 2024-04-29
related_topics:
  - title: English version
    url: /en/linux/debuginfod-find.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debuginfod-find.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debuginfod-find

Solicita datos relacionados con debuginfo.
Más información: <https://manned.org/debuginfod-find>.

- Solicita datos basados en `build_id`:

`debuginfod-find -vv debuginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_build</span>
