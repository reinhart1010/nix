---
layout: page
title: common/brittany (English)
description: "Pretty-print Haskell source files."
content_hash: 4f8c981b2197bd7db97fdfa3c9dc3652e6d71e60
last_modified_at: 2022-12-04
---
# brittany

Pretty-print Haskell source files.
More information: <https://github.com/lspitzner/brittany#readme>.

- Format a Haskell source file and print the result to `stdout`:

`brittany `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>

- Format all Haskell source files in the current directory in-place:

`brittany --write-mode=inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.hs</span>

- Check whether a Haskell source file needs changes and indicate the result through the programme's exit code:

`brittany --check-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>

- Format a Haskell source file using the specified amount of spaces per indentation level and line length:

`brittany --indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --columns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>

- Format a Haskell source file according to the style defined in the specified config file:

`brittany --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>
