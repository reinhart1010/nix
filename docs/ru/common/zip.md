---
layout: page
title: common/zip (русский)
description: "Упаковывает и сжимает (архивирует) файлы в файл zip."
content_hash: 0add65029eebd588bc453b68a5e95c69bda08ff3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

Упаковывает и сжимает (архивирует) файлы в файл zip.
Смотрите также: `unzip`.
Больше информации: <https://manned.org/zip>.

- Добавить файлы/папки в указанный архив ([r]ecursively):

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки1 путь/до/файла_или_папки2 ...</span>

- Удалить файлы/папки из указанного архива ([d]elete):

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки1 путь/до/файла_или_папки2 ...</span>

- Заархивировать файлы/папки, исключая некоторые (e[x]clude):

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки1 путь/до/файла_или_папки2 ...</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/исключаемых_файлов_или_папок</span>

- Заархивировать файлы/папки с заданной степенью сжатия (`0` — без сжатия, `9` — максимальная):

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки1 путь/до/файла_или_папки2 ...</span>

- Создать зашифрованный паролем архив ([e]ncrypted):

`zip -r -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки1 путь/до/файла_или_папки2 ...</span>

- Заархивировать файлы/папки в многотомный архив ([s]plit), например, частями по 3 Гб:

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки1 путь/до/файла_или_папки2 ...</span>

- Вывести содержимое указанного архива ([s]how [f]iles):

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.zip</span>
