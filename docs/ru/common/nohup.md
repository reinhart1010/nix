---
layout: page
title: common/nohup (русский)
description: "Позволяет процессу продолжать работу после закрытия терминала."
content_hash: 631996e461d0d6a32c58457ea29373d1a76a7011
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/nohup.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nohup.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/nohup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nohup

Позволяет процессу продолжать работу после закрытия терминала.
Больше информации: <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

- Запустить процесс, который может выполняться в отвязке от терминала:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">аргумент1 аргумент2 ...</span>

- Запустить `nohup` в фоновом режиме:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">аргумент1 аргумент2 ...</span>` &`

- Запустить скрипт оболочки, который может выполняться в отвязке от терминала:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/скрипта.sh</span>` &`

- Запустить процесс и перенаправить его вывод в указанный файл:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">аргумент1 аргумент2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/выходного_файла</span>` &`
