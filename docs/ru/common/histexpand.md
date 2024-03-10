---
layout: page
title: common/histexpand (русский)
description: "Повторное использование и подстановка команд из списка истории в `sh`, Bash, Zsh, `rbash` and `ksh`."
content_hash: a8015151c89d6a0d6cb6dcd0845f314ede79c6a1
last_modified_at: 2024-03-10
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
tldri18n_status: 2
---
# history expansion

Повторное использование и подстановка команд из списка истории в `sh`, Bash, Zsh, `rbash` and `ksh`.
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
