---
layout: page
title: common/cmark (English)
description: "Converts CommonMark Markdown formatted text to other formats."
content_hash: f83d5cfc5d369e67bd2eee86b69e79d4f3c83587
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

- Convert data from standard input to LaTeX:

`cmark --to latex`

- Convert straight quotes to smart quotes:

`cmark --smart --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>

- Validate UTF-8 characters:

`cmark --validate-utf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.md</span>
