---
layout: page
title: common/ack (русский)
description: "Утилита для поиска, подобная grep, оптимизировання для программистов."
content_hash: 0ceb8dc8819465c760e7db8b4d4d108780b004b5
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

Утилита для поиска, подобная grep, оптимизировання для программистов.
Смотри также: `rg`, которая гораздо быстрее.
Больше информации: <https://beyondgrep.com/documentation>.

- Найти файлы, содержащие строку или регулярное выражение, рекурсивно в текущей директории:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Искать по шаблону без учёта регистра:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Искать строки, соответствующие шаблону, печатая только ([o]nly) совпавший текст, а не остальную часть строки:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Ограничить поиск только файлами определённого типа:

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Не искать в файлах определённого типа:

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Подсчитать общее количество найденных совпадений:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Вывести только имена файлов и количество совпадений для каждого файла:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шаблон_поиска</span>`"`

- Вывести все значения, которые можно использовать с `--type`:

`ack --help-types`
