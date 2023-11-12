---
layout: page
title: common/git-checkout (українська)
description: "Перемикає на гілку чи шлях до робочої директорії."
content_hash: ba4892e1d29104d8b7203178f7681dab77755ce0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout

Перемикає на гілку чи шлях до робочої директорії.
Більше інформації: <https://git-scm.com/docs/git-checkout>.

- Створює та перемикає на нову гілку:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Створює та перемикає на нову гілку спираючись на певне посилання (приклади посилань: гілка, віддалена/гілка, тег):

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">посилання</span>

- Перемикає на локальну гілку, що вже існує:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Перемикає на попередню гілку:

`git checkout -`

- Перемикає на віддалену гілку, що вже існує:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_віддаленого_сховища</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>

- Відкидає усі неіндексовані зміни у поточній директорії (дізнайтесь більше про команди, як скасування, ознайомившись із `git reset`):

`git checkout .`

- Скасовує неіндексовані зміну у файлі:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу</span>

- Замінює файл у поточній директорії на його версію, яку було закомічено до вказаної гілки:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">назва_гілки</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу</span>
