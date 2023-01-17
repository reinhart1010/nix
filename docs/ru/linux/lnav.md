---
layout: page
title: linux/lnav (русский)
description: "Инструмент для просмотра и анализа файлов журналов (логов)."
content_hash: 15f511f416d280944cb0fc1b98515b3a14007256
last_modified_at: 2023-01-17
related_topics:
  - title: English version
    url: /en/linux/lnav.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lnav

Инструмент для просмотра и анализа файлов журналов (логов).
Больше информации: <https://docs.lnav.org/en/latest/cli.html>.

- Просмотреть логи, в качестве аргумента можно указать файл лога, каталог или URL-адрес:

`lnav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_директории|url-адрес</span>

- Просмотреть логи удаленного хоста (требуется аутентификация SSH без пароля):

`lnav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пользователь</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host1.example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/log/syslog.log</span>

- Проверить файлы на соответствие корректности формату логов:

`lnav -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/директории_с_логами</span>
