---
layout: page
title: common/asciidoctor (русский)
description: "Преобразователь AsciiDoc файлов в другие форматы для публикации."
content_hash: 9e9b64b024f0efec02f99278fe5896eed8712f94
last_modified_at: 2023-02-05
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># asciidoctor

Преобразователь AsciiDoc файлов в другие форматы для публикации.
Дополнительная информация: <https://docs.asciidoctor.org>.

- Преобразовать данный `.adoc` файл в HTML (формат на выходе по умолчанию):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.adoc</span>

- Преобразовать данный `.adoc` файл в HTML и привязать к таблице стилей CSS:

`asciidoctor --attribute stylesheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/таблицы-стилей.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.adoc</span>

- Преобразовать данный `.adoc` файл во встраиваемый HTML, убрав всё кроме самого текста:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.adoc</span>

- Преобразовать данный `.adoc` файл в PDF с помощью библиотеки `asciidoctor-pdf`:

`asciidoctor --backend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла.adoc</span>
