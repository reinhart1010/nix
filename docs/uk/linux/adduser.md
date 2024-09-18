---
layout: page
title: linux/adduser (українська)
description: "Утиліта додавання користувачів."
content_hash: 17e9cf5d5b440365ec88728731da09295a199a4a
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/adduser.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adduser

Утиліта додавання користувачів.
Більше інформації: <https://manned.org/adduser>.

- Створити нового користувача з домашнім каталогом за замовчуванням і попросити користувача встановити пароль:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">юзернейм</span>

- Створити нового користувача без домашнього каталогу:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">юзернейм</span>

- Створити нового користувача з домашнім каталогом за вказаним шляхом:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/дому</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">юзернейм</span>

- Створити нового користувача з указаною оболонкою, встановленою як оболонка входу:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/оболонки</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">юзернейм</span>

- Створити нового користувача, що належить до вказаної групи:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">група</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">юзернейм</span>
