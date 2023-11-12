---
layout: page
title: common/head (русский)
description: "Выводит первую часть файлов."
content_hash: 4f252c818e614e62a32a94e0ca743889a8b81163
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/head.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/head.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/head.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/head.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/head.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># head

Выводит первую часть файлов.
Больше информации: <https://manned.org/head.1p>.

- Вывести первые несколько строк из файла:

`head -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количетсво_строк</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_файла</span>

- Вывести первые несколько байтов из файла:

`head -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количество_байт</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_файла</span>

- Вывести все содержимое файла кроме нескольких последних строк:

`head -n -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количетсво_строк</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_файла</span>

- Вывести все содержимое файла кроме нескольких последних байт:

`head -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количество_байт</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя_файла</span>
