---
layout: page
title: common/git-var (Türkçe)
description: "Bir Git mantıksal değişkeninin değerini yazdırır."
content_hash: 9fc23259a3097c84fc9354bc66b726fea638f2c2
related_topics:
  - title: English version
    url: /en/common/git-var.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git var

Bir Git mantıksal değişkeninin değerini yazdırır.
Ayrıca bu komuttan daha çok tercih edilen `git config`'e bakılması önerilir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-var>.

- Yerel bir Git mantıksal değişkeninin değerini yazdır:

`git var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER</span>

- Tüm Git mantıksal değerlerini sırala:

`git var -l`
