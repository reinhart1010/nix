---
layout: page
title: common/git-fetch (українська)
description: "Завантажує об'єкти та посилання з віддаленого сховища."
content_hash: 1408aa4e35c3e45933934862b09e1b59e95fadad
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-fetch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fetch

Завантажує об'єкти та посилання з віддаленого сховища.
Більше інформації: <https://git-scm.com/docs/git-fetch>.

- Отримує останні зміни з віддаленого сховища за замовчуванням (якщо встановлено):

`git fetch`

- Отримує нові гілки з конкретного віддаленого сховища:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_сховища</span>

- Отримує останні зміни з усіх віддалених сховищ:

`git fetch --all`

- Отримує, зокрема, й мітки з віддаленого сховища:

`git fetch --tags`

- Видаляє локальні посилання на віддалені гілки, які були видалені з віддаленого сховища:

`git fetch --prune`
