---
layout: page
title: common/cmark (English)
description: "Convert CommonMark Markdown formatted text to other formats."
content_hash: 688aed8adf7f79aedb942d6e161f5dd7f255a9d8
last_modified_at: 2024-04-26
related_topics:
  - title: italiano version
    url: /it/common/cmark.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmark

Convert CommonMark Markdown formatted text to other formats.
More information: <https://github.com/commonmark/cmark>.

- Render a CommonMark Markdown file to HTML:

`cmark --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>

- Convert data from `stdin` to LaTeX:

`cmark --to latex`

- Convert straight quotes to smart quotes:

`cmark --smart --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>

- Validate UTF-8 characters:

`cmark --validate-utf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>
