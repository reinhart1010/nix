---
layout: page
title: common/histexpand (русский)
description: "Повторное использование и подстановка команд из списка истории в `sh`, `bash`, `zsh`, `rbash` and `ksh`."
content_hash: e40fcbe7f84d126c34935c225701e76410db162c
related_topics:
  - title: English version
    url: /en/common/histexpand.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/histexpand.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/histexpand.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># history expansion

Повторное использование и подстановка команд из списка истории в `sh`, `bash`, `zsh`, `rbash` and `ksh`.
Больше информации: <https://www.gnu.org/software/bash/manual/html_node/History-Interaction>.

- Запустить предыдущую команду от имени суперпользователя (`!!` заменяется на предыдущую команду):

`sudo !!`

- Запустить команду с последним аргументом из предыдущей команды:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` !$`

- Запустить команду с первым аргументом из предыдущей команды:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` !^`

- Запустить `n`-ую с начала команду из истории:

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Запустить `n`-ую с конца команду из истории :

`!-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Запустить самую последнюю команду, содержащую `строка`:

`!?`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">строка</span>`?`

- Запустить предыдущую команду, заменив `строка1` на `строка2`:

`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">строка1</span>`^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">строка2</span>`^`

- Выполнить подстановку команд из списка истории и вывести на экран получившуюся команду, не запуская её:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">!-n</span>`:p`
