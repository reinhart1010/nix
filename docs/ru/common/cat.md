---
layout: page
title: common/cat (русский)
description: "Выводит и объединяет файлы."
content_hash: 1fca1035ee91f793868a232ce20de140f7567223
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cat.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

Выводит и объединяет файлы.
Больше информации: <https://www.gnu.org/software/coreutils/cat>.

- Выводит содержимое файла:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Объединяет несколька файлов в один:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">итоговый_файл</span>

- Добавляет несколько файлов в конец файла:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">итоговый_файл</span>

- Выводит содержимое файла с нумерацией строк:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>

- Показывает все непечатные символы и пробелы (с префиксом `M-` для не-ASCII символов):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">файл</span>
