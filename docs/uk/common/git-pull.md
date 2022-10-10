---
layout: page
title: common/git-pull (українська)
description: "Отримує дані з віддаленого репозиторію та зливає їх із локальним."
content_hash: cac09baef1d3f05c50fc967da91ba74d746b1402
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pull.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-pull.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git pull

Отримує дані з віддаленого репозиторію та зливає їх із локальним.
Більше інформації: <https://git-scm.com/docs/git-pull>.

- Завантажити зміни із типового віддаленого репозиторію та злити їх:

`git pull`

- Завантажити зміни із типового віддаленого репозиторію та злити їх, використовуючи перемотання:

`git pull --rebase`

- Завантажити зміни із певної гілки вказаного віддаленого репозиторію, а потім злити їх у HEAD:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>
