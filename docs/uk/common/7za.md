---
layout: page
title: common/7za (українська)
description: "Архіватор файлів з високим ступенем стиснення."
content_hash: 125532c8683d0990ee9a4c67adfab993976ea58f
last_modified_at: 2024-10-12
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
  - title: русский version
    url: /ru/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7za

Архіватор файлів з високим ступенем стиснення.
Подібний до `7z`, за винятком того, що він підтримує менше типів файлів, але є кросплатформним.
Більше інформації: <https://manned.org/7za>.

- Архівувати ([a]rchive) файл або каталог:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу</span>

- Зашифрувати існуючий архів (включаючи імена файлів):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/зашифрованого_архіву.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пароль</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>

- Розпакувати (e[x]tract) архів, зберігаючи оригінальну структуру каталогів:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>

- Розпакувати (e[x]tract) архів у певний каталог:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/каталогу</span>

- Розпакувати (e[x]tract) архів у `stdout`:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>` -so`

- Архівувати ([a]rchive) за допомогою певного типу архіву:

`7za a -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7z|bzip2|gzip|lzip|tar|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу</span>

- Вивести ([l]ist) перелік вмісту архіву:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>

- Встановити рівень стиснення (вище означає більше стиснення, але повільніше):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.7z</span>` -mx=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|3|5|7|9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу</span>
