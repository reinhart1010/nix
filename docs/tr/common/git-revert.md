---
layout: page
title: common/git-revert (Türkçe)
description: "Öncekilerin etkilerini geri alan yeni bir commit oluştur."
content_hash: d7257069e21f0caf59ea2abf1905d52b47dd6b17
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
# git revert

Öncekilerin etkilerini geri alan yeni bir commit oluştur.
Daha fazla bilgi: <https://git-scm.com/docs/git-revert>.

- En son commit'leri geri al:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@</span>

- En son 5. commit'i geri al:

`git revert HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Birden fazla commit'i geri al:

`git revert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi~5..dal_ismi~2</span>

- Yeni commit'ler oluşturma, yalnızca çalışan ağacı değiştir:

`git revert -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0c01a9..9a1743</span>
