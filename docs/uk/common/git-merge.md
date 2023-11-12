---
layout: page
title: common/git-merge (українська)
description: "Злиття гілок разом."
content_hash: e29635e86bdcfdaa91378ecbec6a22aaaa5d6eec
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
  - title: Türkçe version
    url: /tr/common/git-merge.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git merge

Злиття гілок разом.
Більше інформації: <https://git-scm.com/docs/git-merge>.

- Злиття гілки з поточною гілкою:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Редагує повідомлення при злитті гілок:

`git merge -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Зливає гілки і створює комміт злиття:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Перериває злиття у випадку конфлікту:

`git merge --abort`
