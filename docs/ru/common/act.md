---
layout: page
title: common/act (русский)
description: "Запуск GitHub Actions локально с использованием Docker."
content_hash: c8efb1a0c357907bbd0108f8687aee2300adbfe8
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
---
# act

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
