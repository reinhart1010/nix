---
layout: page
title: osx/cut (русский)
description: "Вырезать поля из стандартного ввода или файлов."
content_hash: f535077d28b08c91d4128512e14f9efe73a97742
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/osx/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Вырезать поля из стандартного ввода или файлов.
Больше информации: <https://manned.org/man/freebsd-13.0/cut.1>.

- Вывести указанный диапазон символов/полей каждой строки (`-c|f 1|1,10|1-10|1-|-10` далее обозначается как `диапазон`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Вывести диапазон каждой строки с указанным разделителем:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">диапазон</span>

- Вывести диапазон каждой строки указанного файла:

`cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
