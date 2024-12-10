---
layout: page
title: common/tex-fmt (English)
description: "Format LaTeX source code."
content_hash: f54c5a822d4638c86505022f7d3d89403ca1bd1a
last_modified_at: 2024-12-10
tldri18n_status: 2
---
# tex-fmt

Format LaTeX source code.
More information: <https://github.com/WGUNDERWOOD/tex-fmt>.

- Format a file, overwriting the original:

`tex-fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Check if a file is correctly formatted:

`tex-fmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Format a file read from `stdin` and print to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>` | tex-fmt --stdin`
