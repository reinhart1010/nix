---
layout: page
title: common/git-merge (Türkçe)
description: "Dalları birleştir."
content_hash: 2357cddbbeaea4d1f6d6686111b6ed60dc99c37e
related_topics:
  - title: English version
    url: /en/common/git-merge.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-merge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-merge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-merge.html
    icon: bi bi-globe
---
# git merge

Dalları birleştir.
Daha fazla bilgi: <https://git-scm.com/docs/git-merge>.

- Mevcut dal ile belirtilen dalı birleştir:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Birleştirme mesajını düzenle:

`git merge -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Bir dalı birleştir ve birleştirme commit'i oluştur:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Karışıklık durumlarına karşı birleştirme işlemini durdur:

`git merge --abort`
