---
layout: page
title: common/jq (русский)
description: "Процессор JSON командной строки, использующий доменный язык."
content_hash: c8065c6d6b24472f0b6ff96d81b91dfa5a960f0e
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/jq.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jq

Процессор JSON командной строки, использующий доменный язык.
Больше информации: <https://stedolan.github.io/jq/manual/>.

- Выполнить указанное выражение (вывести цветной и отформатированный JSON):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '.'`

- Выполнить указанный скрипт:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq --from-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/скрипту.jq</span>

- Передать указанные агрументы:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--arg "имя1" "значение1" --arg "имя2" "значение2" ...</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">. + $ARGS.named</span>`'`

- Вывести указанные ключи:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ключ1, .ключ2, ...</span>`'`

- Вывести указанные элементы массива:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[индекс1], .[индекс2], ...</span>`'`

- Вывести все элементы массива/ключи объекта:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '.[]'`

- Добавить/удалить указанные ключи:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ключ1": "значение1", "ключ2": "значение2", ...}</span>`'`
