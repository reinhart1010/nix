---
layout: page
title: common/history (русский)
description: "История командной строки."
content_hash: aa7d78f2cb5c6f9519ee99528d387f62b9cf43b4
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# history

История командной строки.
Больше информации: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Отобразить список истории команд с номерами строк:

`history`

- Отобразить последние 20 команд (в `zsh` отображает все команды, начиная с 20-й):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Очистить список истории команд (только для текущей оболочки `bash`):

`history -c`

- Перезаписать файл истории историей текущей оболочки `bash` (часто комбинируется с `history -c` для очистки истории):

`history -w`

- Удалить элемент истории с указанным номером:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">номер</span>
