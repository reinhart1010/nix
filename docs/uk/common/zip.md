---
layout: page
title: common/zip (українська)
description: "Утиліта архівування файлів в Zip-архів."
content_hash: 84a238fecc403b11c5305669e3ed8838c423a9d6
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zip.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/zip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

Утиліта архівування файлів в Zip-архів.
Дивіться також: `unzip`.
Більше інформації: <https://manned.org/zip>.

- Додати файли/каталоги до певного архіву рекурсивно ([r]ecursively):

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу1 шлях/до/файлу_або_каталогу2 ...</span>

- Видалити файли/каталоги із певного архіву ([d]elete):

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу1 шлях/до/файлу_або_каталогу2 ...</span>

- Архівувати файли/каталоги, окрім (e[x]cluding) зазначених:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу1 шлях/до/файлу_або_каталогу2 ...</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/виключених_файлів_або_каталогів</span>

- Архівувати файли/каталоги з певним рівнем стиснення (`0` - найнижчий, `9` - найвищий):

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу1 шлях/до/файлу_або_каталогу2 ...</span>

- Створити зашифрований ([e]ncrypted) архів із певним паролем (з’явиться запит на введення пароля):

`zip -r -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу1 шлях/до/файлу_або_каталогу2 ...</span>

- Архівувати файли/каталоги в архів з багатьох частин ([s]split) (наприклад, частини по 3 Гб):

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_каталогу1 шлях/до/файлу_або_каталогу2 ...</span>

- Print a specific archive contents Вивести перелік вмісту певного архіву:

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/архіву.zip</span>
