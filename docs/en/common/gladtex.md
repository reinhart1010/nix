---
layout: page
title: common/gladtex (English)
description: "A LaTeX formula preprocessor for HTML files."
content_hash: 9e7f329eb6ce2b05c27103621c6ef6f52eaf9be5
last_modified_at: 2023-10-10
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gladtex

A LaTeX formula preprocessor for HTML files.
It converts LaTeX formulas to images.
More information: <https://humenda.github.io/GladTeX/manpage.html/>.

- Convert to html:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.htex</span>

- Save the converted file to a specific location:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.htex</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.html</span>

- Save the generated images to a specific [d]irectory:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.htex</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_output_directory</span>

- Set image [r]esolution (in dpi, default is 100):

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.htex</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resolution</span>

- [k]eep LaTeX files after conversion:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.htex</span>` -k`

- Set [b]ackground and [f]oreground color of the images:

`gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.htex</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">background_color</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foreground_color</span>

- Convert Markdown to HTML using `pandoc` and `gladtex`:

`pandoc -s -t html --gladtex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.md</span>` | gladtex -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.html</span>
