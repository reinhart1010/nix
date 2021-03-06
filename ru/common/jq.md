---
layout: page
title: common/jq (русский)
description: "Процессор JSON командной строки, использующий доменный язык."
content_hash: 7a4531442886c51755f2f1aad6363e6104a2dcc4
related_topics:
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
---
# jq

Процессор JSON командной строки, использующий доменный язык.
Больше информации: <https://stedolan.github.io/jq/manual/>.

- Выполнить указанное выражение (вывести цветной и отформатированный json):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>`'`

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

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat путь/к/файлу.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"ключ1": "значение1", "ключ2": "значение2", ...</span>`}'`
