---
layout: page
title: common/tectonic (English)
description: "A modern, self-contained TeX/LaTeX engine."
content_hash: 7d597f3c9d85089675d94f25399d446a764a6500
last_modified_at: 2023-07-25
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tectonic

A modern, self-contained TeX/LaTeX engine.
More information: <https://tectonic-typesetting.github.io/book/latest>.

- Compile a standalone TeX/LaTeX file:

`tectonic -X compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Compile a standalone TeX/LaTeX file with synctex data:

`tectonic -X compile --synctex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.tex</span>

- Initialize a tectonic project in the current directory:

`tectonic -X init`

- Initialize a tectonic project in the specified directory:

`tectonic -X new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Build the project in the current directory:

`tectonic -X build`

- Start a watcher to build the project in the current directory on change:

`tectonic -X watch`
