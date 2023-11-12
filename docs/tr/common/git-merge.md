---
layout: page
title: common/git-merge (Türkçe)
description: "Dalları birleştir."
content_hash: 8b087f1c53e05800d4406fd83f19302bbd2cadd7
last_modified_at: 2023-11-12
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
  - title: українська version
    url: /uk/common/git-merge.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git merge

Dalları birleştir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-merge>.

- Mevcut dal ile belirtilen dalı birleştir:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Birleştirme mesajını düzenle:

`git merge -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Bir dalı birleştir ve birleştirme commit'i oluştur:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Karışıklık durumlarına karşı birleştirme işlemini durdur:

`git merge --abort`
