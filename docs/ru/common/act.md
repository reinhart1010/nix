---
layout: page
title: common/act (русский)
description: "Запуск GitHub Actions локально с использованием Docker."
content_hash: c8efb1a0c357907bbd0108f8687aee2300adbfe8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># act

Запуск GitHub Actions локально с использованием Docker.
Больше информации: <https://github.com/nektos/act>.

- Вывести список доступных actions:

`act -l`

- Запустить событие по умолчанию:

`act`

- Запустить заданное событие:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">тип_события</span>

- Запустить заданный action:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- Не производить реальный запуск actions (пробный прогон):

`act -n`

- Отображать расширенный лог:

`act -v`
