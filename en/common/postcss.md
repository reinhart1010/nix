---
layout: page
title: common/postcss (English)
description: "PostCSS is a tool for transforming styles with JS plugins."
content_hash: 2a2bd1687f2c3b17c57f3b998a74010df3940c7b
---
# postcss

PostCSS is a tool for transforming styles with JS plugins.
More information: <https://postcss.org>.

- Parse and transform a CSS file:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Parse and transform a CSS file and output to a specific file:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Parse and transform a CSS file and output to a specific directory:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Parse and transform a CSS file in-place:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --replace`

- Specify a custom PostCSS parser:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --parser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parser</span>

- Specify a custom PostCSS syntax:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --syntax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">syntax</span>

- Watch for changes to a CSS file:

`postcss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --watch`

- Display available options and examples:

`postcss --help`
