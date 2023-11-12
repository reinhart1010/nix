---
layout: page
title: common/ebook-convert (English)
description: "Can be used to convert e-books between common formats, e.g. PDF, EPUB and MOBI."
content_hash: c1eaebb834d586183b945c323bfb391b8277c8f6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ebook-convert.html
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

Can be used to convert e-books between common formats, e.g. PDF, EPUB and MOBI.
Part of the Calibre e-book library tool.
More information: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Convert an e-book into another format:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>

- Convert Markdown or HTML to e-book with TOC, title and author:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>` --authors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>
