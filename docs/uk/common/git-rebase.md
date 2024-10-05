---
layout: page
title: common/git-rebase (українська)
description: "Повторно застосовує коміти з однієї гілки поверх іншої."
content_hash: f4895f56ffecb4b6f246ad95d41338d31ff146e0
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Повторно застосовує коміти з однієї гілки поверх іншої.
Зазвичай використовується для дублювання комітів з однієї гілки до іншої, шляхом створення нових комітів у гілці призначення.
Більше інформації: <https://git-scm.com/docs/git-rebase>.

- Перебазовує активну гілку поверх іншої, вказаної гілки:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">нова_базова_гілка</span>

- Розпочинає інтерактивне перебазування, яке дозволяє змінювати порядок, оминати, об'єднувати чи редагувати коміти:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">цільова_базова_гілка_або_хеш_коміту</span>

- Продовжує перебазування перерване через збій злиття після виправлення конфліктних файлів:

`git rebase --continue`

- Продовжує перебазування призупинене через конфлікти при злитті, пропустивши конфліктний коміт:

`git rebase --skip`

- Перериває поточне перебазування (наприклад, якщо воно було перерване через конфлікт при злитті):

`git rebase --abort`

- Переносить частину поточної гілки поверх нової бази, використавши стару базу, як початок:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">нова_база</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">стара_база</span>

- Повторно застосовує останні 5 комітів, зупиняючись аби змінювати порядок, оминати, об'єднувати чи редагувати їх:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Автоматично вирішує будь-які конфлікти надавши перевагу робочій версії гілки (ключ `theirs` має обернене значення в цьому випадку):

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-X|--strategy-option</span>` theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>
