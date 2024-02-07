---
layout: page
title: linux/man (русский)
description: "Утилита просмотра справочных страницs."
content_hash: 8ba334083e435bd296dfc03cbd520ef5be1e3e5a
last_modified_at: 2024-02-07
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/man.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/man.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/man.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

Утилита просмотра справочных страницs.
Больше информации: <https://manned.org/man>.

- Показать справочную страницу для команды:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Показать справочную страницу пакета макросов команды из раздела:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Отобразить краткое описание из справочной страницы, если оно есть:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Отобразить путь поиска справочных страниц:

`man --path`

- Отобразить расположение справочной страницы, а не саму справочную страницу:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Отобразить справочную страницу с использованием определённой локали:

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">локаль</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Найти справочную страницу, содержащую строку поиска:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">строка_поиска</span>`"`
