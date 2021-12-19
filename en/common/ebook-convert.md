---
layout: page
title: common/ebook-convert (English)
description: "Can be used to convert e-books between common formats, e.g. PDF, EPUB and MOBI."
content_hash: 81a0d13603c507a51982e5aab08c65f0ca201f89
related_topics:
  - title: italiano version
    url: /it/common/ebook-convert.html
    icon: bi bi-globe
---
# ebook-convert

Can be used to convert e-books between common formats, e.g. PDF, EPUB and MOBI.
Part of the Calibre e-book library tool.
More information: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Convert an e-book into another format:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>

- Convert Markdown or HTML to e-book with TOC, title and author:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>` --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>` --authors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>
