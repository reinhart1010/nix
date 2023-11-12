---
layout: page
title: common/pygmentize (English)
description: "Python-based syntax highlighter."
content_hash: f334408808c42ac7b924a4bc452119f636d7c7b8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pygmentize

Python-based syntax highlighter.
More information: <https://pygments.org/docs/cmdline/>.

- Highlight file syntax and print to `stdout` (language is inferred from the file extension):

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
