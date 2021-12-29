---
layout: page
title: common/git-grep (Türkçe)
description: "Belirtilen söz dizisini bir deponun geçmişi dahil tüm dosyalarında ara."
content_hash: 8ee92e9db67eb8c4719ca19320fff454a44ec6c1
related_topics:
  - title: English version
    url: /en/common/git-grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-grep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-grep.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git-grep

Belirtilen söz dizisini bir deponun geçmişi dahil tüm dosyalarında ara.
Sıradan `grep` komutundaki birçok ek bu komut için de aynen geçerlidir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-grep>.

- İzlenen dosyalarda belirtilen söz dizisini ara:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">söz_dizisi</span>

- İzlenen dosyalarda belirtilen desene uygun, belirtilen söz dizisini ara:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">söz_dizisi</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_glob_pattern</span>

- Alt modüller de dahil olmak üzere izlenen dosyalarda belirtilen söz dizisini ara:

`git grep --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">söz_dizisi</span>

- Belirtilen depo geçmişinde belirtilen söz dizisini ara:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">söz_dizisi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>

- Belirtilen söz dizisini tüm dallarda ara:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">söz_dizisi</span>` $(git rev-list --all)`
