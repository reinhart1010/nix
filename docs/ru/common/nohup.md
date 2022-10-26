---
layout: page
title: common/nohup (русский)
description: "Позволяет процессу продолжать работу после закрытия терминала."
content_hash: e642ccabc0e40fa3fdcc17d4fbd6612f3e413c1b
related_topics:
  - title: English version
    url: /en/common/nohup.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nohup

Позволяет процессу продолжать работу после закрытия терминала.
Больше информации: <https://www.gnu.org/software/coreutils/nohup>.

- Запустить процесс, который может выполняться в отвязке от терминала:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">аргументы_команды</span>

- Запустить `nohup` в фоновом режиме:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">аргументы_команды</span>` &`

- Запустить скрипт оболочки, который может выполняться в отвязке от терминала:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/скрипта.sh</span>` &`

- Запустить процесс и перенаправить его вывод в указанный файл:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">аргументы_команды</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного_файла</span>` &`
