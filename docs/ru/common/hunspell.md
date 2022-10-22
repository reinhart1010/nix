---
layout: page
title: common/hunspell (русский)
description: "Проверка орфографии."
content_hash: fb27e531e20141bf968b1f287ffe1cb5ae2b54f1
related_topics:
  - title: English version
    url: /en/common/hunspell.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hunspell

Проверка орфографии.
Больше информации: <https://hunspell.github.io/>.

- Проверить орфографию в указанном файле:

`hunspell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Проверить орфографию в указанном файле, используя американский словарь (en_US):

`hunspell -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_US</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Вывести список неправильно написанных слов в файле:

`hunspell -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>
