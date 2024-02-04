---
layout: page
title: osx/cut (русский)
description: "Вырезать поля из стандартного ввода или файлов."
content_hash: 5a5098d4c9f9c37edf6e7f8fc8775348f03b76af
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/osx/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/cut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Вырезать поля из стандартного ввода или файлов.
Больше информации: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- Вывести указанный диапазон символов/полей каждой строки (`-c|f 1|1,10|1-10|1-|-10` далее обозначается как `диапазон`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` | cut -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|f</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Вывести диапазон полей каждой строки с указанным разделителем:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>` | cut -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">диапазон</span>

- Вывести диапазон символов каждой строки указанного файла:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
