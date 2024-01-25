---
layout: page
title: common/brittany (English)
description: "Pretty-print Haskell source files."
content_hash: 40ee94e348f62a2a9b225c00bb4ab0d53c8fe7e0
last_modified_at: 2024-01-25
tldri18n_status: 2
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

- Format a Haskell source file according to the style defined in the specified configuration file:

`brittany --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>
