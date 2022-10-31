---
layout: page
title: common/git-init (Türkçe)
description: "Yeni bir yerel Git deposu başlat."
content_hash: be86cce41f4c3d24f1680d55aa25d3b68a6bd970
related_topics:
  - title: Deutsch version
    url: /de/common/git-init.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-init.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-init.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-init.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-init.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-init.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git init

Yeni bir yerel Git deposu başlat.
Daha fazla bilgi için: <https://git-scm.com/docs/git-init>.

- Yeni bir yerel depo başlat:

`git init`

- Bir depoyu nesne verileri için SHA256 formatı ile başlat (Git versiyonu 2.29 veya üstü olmalıdır):

`git init --object-format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha256</span>

- Yalın bir depo başlat:

`git init --bare`
