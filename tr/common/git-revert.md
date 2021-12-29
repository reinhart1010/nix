---
layout: page
title: common/git-revert (Türkçe)
description: "Öncekilerin etkilerini geri alan yeni bir commit oluştur."
content_hash: fabb19c6fe2bb38b29678d27ac8058aaa25775ad
related_topics:
  - title: English version
    url: /en/common/git-revert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-revert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-revert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-revert.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git revert

Öncekilerin etkilerini geri alan yeni bir commit oluştur.
Daha fazla bilgi için: <https://git-scm.com/docs/git-revert>.

- En son commit'leri geri al:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@</span>

- En son 5. commit'i geri al:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Birden fazla commit'i geri al:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi~5..dal_ismi~2</span>

- Yeni commit'ler oluşturma, yalnızca çalışan ağacı değiştir:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
