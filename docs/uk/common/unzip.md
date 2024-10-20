---
layout: page
title: common/unzip (українська)
description: "Утиліта розпакування файлів/каталогів з Zip архівів."
content_hash: 7695a1ac5457f252835603ec84618065376ed7fe
last_modified_at: 2024-10-20
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
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unzip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unzip

Утиліта розпакування файлів/каталогів з Zip архівів.
Дивіться також: `zip`.
Більше інформації: <https://manned.org/unzip>.

- Розпакувати всі файли/каталоги з певних архівів у поточний каталог:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву1.zip шлях/до/архіву2.zip ...</span>

- Розпакувати файли/каталоги з архівів у певний шлях:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву1.zip шлях/до/архіву2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/виводу</span>

- Розпакувати файли/каталоги з архівів у `stdout` разом із виводом імен файлів:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву1.zip шлях/до/архіву2.zip ...</span>

- Розпакувати архів, створений у Windows, який містить файли з назвами файлів, відмінними від ASCII (наприклад, китайськими чи японськими символами):

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву1.zip шлях/до/архіву2.zip ...</span>

- Вивести ([l]ist) перелік вмісту певного архіву, не розпаковуючи його:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>

- Розпакувати певний файл з архіву:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1_в_архіві шлях/до/файлу2_в_архіві ...</span>
