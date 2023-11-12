---
layout: page
title: common/git-commit-graph (українська)
description: "Записує та перевіряє файл графіку комітів Git."
content_hash: 39ad65661fec71295da66d293e3cb70206a611a3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-commit-graph.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit-graph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-graph

Записує та перевіряє файл графіку комітів Git.
Більше інформації: <https://git-scm.com/docs/git-commit-graph>.

- Записує файл графіку комітів для спакованих комітів у локальній директорії `.git`:

`git commit-graph write`

- Записує файл графіку комітів, що містить набір усіх досяжних комітів:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Записує файл графіку комітів, що містить усі коміти у поточному файлі графіку комітів разом з тими, до яких можна отримати доступ з `HEAD`:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` | git commit-graph write --stdin-commits --append`
