---
layout: page
title: common/cmark (English)
description: "Converts CommonMark Markdown formatted text to other formats."
content_hash: 9e22c86e73e8ecc8e81817d5987d6dece48a36e3
last_modified_at: 2023-08-09
related_topics:
  - title: italiano version
    url: /it/common/cmark.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmark.html
    icon: bi bi-globe
---
# cmark

Converts CommonMark Markdown formatted text to other formats.
More information: <https://github.com/commonmark/cmark>.

- Render a CommonMark Markdown file to HTML:

`cmark --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>

- Convert data from `stdin` to LaTeX:

`cmark --to latex`

- Convert straight quotes to smart quotes:

`cmark --smart --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>

- Validate UTF-8 characters:

`cmark --validate-utf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>
