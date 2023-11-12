---
layout: page
title: common/zsh (русский)
description: "Z SHell — командный интерпретатор, совместимый с Bash."
content_hash: 1e586e1808999f059fdcc8f37dbf0b6d538cc773
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zsh

Z SHell — командный интерпретатор, совместимый с Bash.
Смотри также `histexpand` про подстановку команд из списка истории.
Больше информации: <https://www.zsh.org>.

- Запустить интерактивную сессию оболочки:

`zsh`

- Выполнить команду и выйти:

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>`"`

- Выполнить скрипт:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/скрипта.zsh</span>

- Выполнить скрипт с выводом каждой команды перед её выполнением:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/скрипта.zsh</span>

- Запустить интерактивную сессию оболочки в подробном режиме, выводя каждую команду перед её выполнением:

`zsh --verbose`

- Выполнить определённую команду внутри `zsh` с отключёнными glob-шаблонами:

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>
