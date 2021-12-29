---
layout: page
title: common/git-show-branch (Türkçe)
description: "Dalları ve içerdikleri commit'leri göster:"
content_hash: 1fbe28158afac6b62c81dbf915e30e502c2001b4
related_topics:
  - title: English version
    url: /en/common/git-show-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-branch.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git show-branch

Dalları ve içerdikleri commit'leri göster:
Daha fazla bilgi için: <https://git-scm.com/docs/git-show-branch>.

- Bir daldaki son commit'lerin bir özetini göster:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi|referans|commit</span>

- Çeşitli commit veya daldaki commit'lerin geçmişini karşılaştır:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi|referans|commit</span>

- Tüm uzak takip dallarını karşılaştır:

`git show-branch --remotes`

- Hem yerel, hem de uzak takip dallarını karşılaştır:

`git show-branch --all`

- Tüm dallardaki son commit'leri sırala:

`git show-branch --all --list`

- Belirtilen dalı mevcut dal ile karşılaştır:

`git show-branch --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|dal_ismi|referans</span>

- Bağlı isim yerine commit ismini görüntüle:

`git show-branch --sha1-name --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current|dal_ismi|referans</span>

- Commit'lerin ortak atasından sonraki commit'leri belirtilen sayı kadar görüntüle:

`git show-branch --more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|dal_ismi|referans</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|dal_ismi|referans</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>
