---
layout: page
title: common/hunspell (русский)
description: "Проверка орфографии."
content_hash: e280fcfadeb26b60c8e040b5602ebaa94e6a9be8
related_topics:
  - title: English version
    url: /en/common/hunspell.html
    icon: bi bi-globe
---
# hunspell

Проверка орфографии.
Больше информации: <https://github.com/hunspell/hunspell>.

- Проверить орфографию в указанном файле:

`hunspell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Проверить орфографию в указанном файле, используя американский словарь (en_US):

`hunspell -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_US</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Вывести список неправильно написанных слов в файле:

`hunspell -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>
