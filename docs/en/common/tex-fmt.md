---
layout: page
title: common/tex-fmt (English)
description: "Format LaTeX source code."
content_hash: f54c5a822d4638c86505022f7d3d89403ca1bd1a
last_modified_at: 2024-12-09
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tex-fmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tex-fmt

Format LaTeX source code.
More information: <https://github.com/WGUNDERWOOD/tex-fmt>.

- Format a file, overwriting the original:

`tex-fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Check if a file is correctly formatted:

`tex-fmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Format a file read from `stdin` and print to `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>` | tex-fmt --stdin`
