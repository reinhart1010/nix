---
layout: page
title: common/chroma (English)
description: "Chroma is a general-purpose syntax highlighting library and corresponding command, for Go."
content_hash: a3708497d4f1571884e5761a2d9de35a6c22957a
last_modified_at: 2023-05-02
---
# chroma

Chroma is a general-purpose syntax highlighting library and corresponding command, for Go.
More information: <https://github.com/alecthomas/chroma>.

- Highlight a source file with Python lexer and output to terminal:

`chroma --lexer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>

- Highlight a source file with the Go lexer and output to an HTML file:

`chroma --lexer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go</span>`" --formatter="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html_file</span>

- Highlight a source file with the C++ lexer and output to an SVG, using the Monokai style:

`chroma --lexer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++</span>`" --formatter="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>`" --syle="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monokai</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg_file</span>
