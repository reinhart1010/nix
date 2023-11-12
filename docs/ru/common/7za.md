---
layout: page
title: common/7za (русский)
description: "Архиватор файлов с высокой степенью сжатия."
content_hash: d71b5350044c1ea03cf73c89e99037f620883bf3
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/7za.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7za.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7za.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7za.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7za.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7za.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/7za.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7za.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7za.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7za.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7za.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7za.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7za.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7za.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7za

Архиватор файлов с высокой степенью сжатия.
То же, что и `7z`, за исключением того, что поддерживает меньшее количество типов файлов, но является кроссплатформенным.
Больше информации: <https://manned.org/7za>.

- Архивировать ([a]rchive) файл или папку:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки</span>

- Зашифровать существующий архив (включая имена файлов):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/зашифрованного_архива.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пароль</span>` -mhe=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>

- Распаковать (e[x]tract) существующий архив, сохраняя оригинальную структуру папок:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>

- Распаковать (e[x]tract) архив в нужную папку:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>

- Распаковать (e[x]tract) архив в `stdout`:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>` -so`

- Архивировать ([a]rchive), используя определённый тип архива:

`7za a -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7z|bzip2|gzip|lzip|tar|zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_или_папки</span>

- Вывести ([l]ist) содержимое архива:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/архива.7z</span>

- Вывести список всех доступных типов архивов:

`7za i`
