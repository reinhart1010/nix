---
layout: page
title: common/cmark (italiano)
description: "Converte testo CommonMark Markdown in altri formati."
content_hash: 46f2e08b392fffd46f7c378f5f7a34ff447673fd
related_topics:
  - title: English version
    url: /en/common/cmark.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmark.html
    icon: bi bi-globe
---
# cmark

Converte testo CommonMark Markdown in altri formati.
Maggiori informazioni: <https://github.com/commonmark/cmark>.

- Converti un file Markdown in HTML:

`cmark --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.md</span>

- Converti in LaTeX da standard input:

`cmark --to latex`

- Converti apici semplici in apici intelligenti:

`cmark --smart --to html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.md</span>

- Converti validando i caratteri UTF-8:

`cmark --validate-utf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.md</span>
