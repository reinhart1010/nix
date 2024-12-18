---
layout: page
title: common/echo (русский)
description: "Отобразить заданные аргументы."
content_hash: 8ae0c9f1265733f784ab2def1adbdecda9b0a66f
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/echo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/echo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/echo.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/echo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/echo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/echo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/echo.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/echo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># echo

Отобразить заданные аргументы.
Больше информации: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Отобразить текстовое сообщение. Примечание: кавычки необязательны:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Привет, мир</span>`"`

- Отобразить сообщение с переменной окружения:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Мой путь - $PATH</span>`"`

- Отобразить сообщение, не перенося каретку на новую строку:

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Привет, мир</span>`"`

- Добавить сообщение в файл:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Привет, мир</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/к/файлу.txt</span>

- Экранировать с помощью символа обратной косой черты (специальный символ):

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Column 1\tColumn 2</span>`"`
