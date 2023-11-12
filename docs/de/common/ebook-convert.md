---
layout: page
title: common/ebook-convert (Deutsch)
description: "Kann verwendet werden, um E-Books zu geläufigen Dateiformaten umzuwandeln, z.B. PDF, EPUB und MOBI."
content_hash: 3978fa95012e01de4f431a1a908402be94d37cbe
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ebook-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ebook-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ebook-convert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ebook-convert

Kann verwendet werden, um E-Books zu geläufigen Dateiformaten umzuwandeln, z.B. PDF, EPUB und MOBI.
Teil der Calibre e-book library.
Weitere Informationen: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Konvertiere ein E-Book in ein anderes Format:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/input_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/output_datei</span>

- Konvertiere eine Markdown- oder HTML Datei zu einem E-Book inklusive Inhaltsverzeichnis, Titel und Autoren:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/input_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/output_datei</span>` --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">titel</span>` --authors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>
