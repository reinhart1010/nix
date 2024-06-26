---
layout: page
title: common/md-to-clip (English)
description: "Convert tldr-pages to Command Line Interface Pages."
content_hash: 02012ab0cc9a9e2e48beb177a029298677bfce33
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# md-to-clip

Convert tldr-pages to Command Line Interface Pages.
See also: `clip-view`.
More information: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>.

- Convert tldr-pages files and save into the same directories:

`md-to-clip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/page1.md path/to/page2.md ...</span>

- Convert tldr-pages files and save into a specific directory:

`md-to-clip --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/page1.md path/to/page2.md ...</span>

- Convert a tldr-page file to `stdout`:

`md-to-clip --no-file-save <(echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page-content</span>`')`

- Convert tldr-pages files while recognizing additional placeholders from a specific config:

`md-to-clip --special-placeholder-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/page1.md path/to/page2.md ...</span>

- Display help:

`md-to-clip --help`

- Display version:

`md-to-clip --version`
