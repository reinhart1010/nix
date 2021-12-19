---
layout: page
title: common/unzip (русский)
description: "Извлекает сжатые файлы из архива zip."
content_hash: abdfa68cbe789ae93310deec97c1f5ac3be4a229
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
---
# unzip

Извлекает сжатые файлы из архива zip.

- Распаковать файл(ы) zip (для нескольких файлов укажите пути через пробел):

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив(ы)</span>

- Распаковать файл(ы) по нужному пути:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив(ы)</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/путь/куда/положить/извлечённый_файл(ы)</span>

- Вывести список файлов в архиве zip, не распаковывая их:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив.zip</span>

- Извлечь содержимое файла в stdout вместе с именами распакованных файлов:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив.zip</span>

- Распаковать архив zip, который был создан на windows и содержит не-ascii имена файлов (напр. кириллица):

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">архив.zip</span>
