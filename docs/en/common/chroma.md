---
layout: page
title: common/chroma (English)
description: "A general-purpose syntax highlighter."
content_hash: 78cecf5f35b529b2998d50421fec6f8c3a5a1b17
last_modified_at: 2023-05-17
---
# chroma

A general-purpose syntax highlighter.
The `--lexer` option is usually unnecessary, as it will be automatically determined based on the file extension.
More information: <https://github.com/alecthomas/chroma>.

- Highlight source code from a file with the Python lexer and output to `stdout`:

`chroma --lexer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.py</span>

- Highlight source code from a file with the Go lexer and output to an HTML file:

`chroma --lexer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go</span>` --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.go</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_file.html</span>

- Highlight source code from `stdin` with the C++ lexer and output to an SVG file, using the Monokai style:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | chroma --lexer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c++</span>` --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monokai</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_file.svg</span>

- List available lexers, styles and formatters:

`chroma --list`
