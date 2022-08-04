---
layout: page
title: common/pygmentize (English)
description: "Python-based syntax highlighter."
content_hash: 77385ec8c141e4cf0ad809175bc596fa5dae6873
---
# pygmentize

Python-based syntax highlighter.
More information: <https://pygments.org/docs/cmdline/>.

- Highlight file syntax and print to standard output (language is inferred from the file extension):

`pygmentize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Explicitly set the language for syntax highlighting:

`pygmentize -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">javascript</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- List available lexers (processors for input languages):

`pygmentize -L lexers`

- Save output to a file in HTML format:

`pygmentize -f html -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file.py</span>

- List available output formats:

`pygmentize -L formatters`

- Output an HTML file, with additional formatter options (full page, with line numbers):

`pygmentize -f html -O "full,linenos=True" -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>
