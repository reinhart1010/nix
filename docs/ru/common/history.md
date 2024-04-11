---
layout: page
title: common/history (русский)
description: "История командной строки."
content_hash: 269704d3287130c6cba065b98af111d1b809270f
last_modified_at: 2024-04-11
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/history.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># history

История командной строки.
Больше информации: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Отобразить список истории команд с номерами строк:

`history`

- Отобразить последние 20 команд (в Zsh отображает все команды, начиная с 20-й):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Очистить список истории команд (только для текущей оболочки Bash):

`history -c`

- Перезаписать файл истории историей текущей оболочки Bash (часто комбинируется с `history -c` для очистки истории):

`history -w`

- Удалить элемент истории с указанным номером:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">номер</span>
