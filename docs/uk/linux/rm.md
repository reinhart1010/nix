---
layout: page
title: linux/rm (українська)
description: "Видалити файли або директорії."
content_hash: ea506df0ef241aea2e8b3a3baeba8f5b480eb749
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/linux/rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rm.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rm

Видалити файли або директорії.
Дивіться також: `rmdir`.
Більше інформації: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Видалити певні файли:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1 шлях/до/файлу2 ...</span>

- Видалити певні файли, ігноруючи неіснуючі:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1 шлях/до/файлу2 ...</span>

- Видалити певні файли інтерактивно запитуючи перед кожним видаленням:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1 шлях/до/файлу2 ...</span>

- Видалити певні файли, друкуючи інформацію про кожне видалення:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу1 шлях/до/файлу2 ...</span>

- Видалити певні файли та директорії рекурсивно:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_або_папки1 шлях/до/файлу_або_папки2 ...</span>
