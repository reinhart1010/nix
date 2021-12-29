---
layout: page
title: common/git-rev-parse (Türkçe)
description: "Belirtilen sürümler için metaveri görüntüle."
content_hash: 1e8a53c724130b49fffa63f1d725e2481c296cc9
related_topics:
  - title: English version
    url: /en/common/git-rev-parse.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-parse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-parse.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-parse.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git rev-parse

Belirtilen sürümler için metaveri görüntüle.
Daha fazla bilgi için: <https://git-scm.com/docs/git-rev-parse>.

- Bir dalın commit verisini göster:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Mevcut dal ismini göster:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Kök dizinin mutlak konumunu göster:

`git rev-parse --show-toplevel`
