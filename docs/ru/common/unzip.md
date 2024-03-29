---
layout: page
title: common/unzip (русский)
description: "Извлекает сжатые файлы из архива zip."
content_hash: 16ffd5741c41b7d72d787e1d4b9250f57afe84f6
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unzip

Извлекает сжатые файлы из архива zip.
Больше информации: <https://manned.org/unzip>.

- Распаковать файл(ы) zip (для нескольких файлов укажите пути через пробел):

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив(ы)</span>

- Распаковать файл(ы) по нужному пути:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив(ы)</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/путь/куда/положить/извлечённый_файл(ы)</span>

- Вывести список файлов в архиве zip, не распаковывая их:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив.zip</span>

- Извлечь содержимое файла в `stdout` вместе с именами распакованных файлов:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив.zip</span>

- Распаковать архив zip, который был создан на windows и содержит не-ascii имена файлов (напр. кириллица):

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив.zip</span>
