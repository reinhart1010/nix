---
layout: page
title: common/abduco (русский)
description: "Менеджер сессий терминала."
content_hash: cdb2bdf53ba938cdd7e804993ff6b70e0668abe4
related_topics:
  - title: English version
    url: /en/common/abduco.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/abduco.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/abduco.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/abduco.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/abduco.html
    icon: bi bi-globe
---
# abduco

Менеджер сессий терминала.
Больше информации: <http://www.brain-dump.org/projects/abduco/>.

- Вывести список сеансов:

`abduco`

- Подключиться к сеансу, и создать его, если он не существует:

`abduco -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- Подключиться к сеансу с `dvtm`, и создать его, если он не существует:

`abduco -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя</span>

- Отключиться от сеанса:

`Ctrl + \`

- Подключиться к сеансу в режиме только для чтения:

`abduco -Ar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя</span>
