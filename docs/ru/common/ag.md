---
layout: page
title: common/ag (русский)
description: "The Silver Searcher. Аналог `ack`, но имеет цель быть быстрее."
content_hash: f5d47c6222b99364903b34034f531d158b1f23cd
last_modified_at: 2023-12-03
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ag

The Silver Searcher. Аналог `ack`, но имеет цель быть быстрее.
Больше информации: <https://github.com/ggreer/the_silver_searcher>.

- Найти файлы, содержащие "foo", и вывести подходящие строки в контексте:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Найти файлы, содержащие "foo", в заданной папке:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>

- Найти файлы, содержащие "foo", но вывести только имена файлов:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Найти файлы, содержащие "FOO", независимо от регистра, и вывести только совпадения, а не строки целиком:

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- Найти "foo" в файлах, у которых в имени есть "bar":

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Найти файлы, содержимое которых совпадает с регулярным выражением:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- Найти файлы, у которых имя совпадает с "foo":

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
