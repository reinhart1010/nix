---
layout: page
title: common/git-merge (українська)
description: "Злиття гілок разом."
content_hash: b348be5a77f819f138749d2342ba59215820794a
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-merge.html
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

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Зливає гілки і створює комміт злиття:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Перериває злиття у випадку конфлікту:

`git merge --abort`
