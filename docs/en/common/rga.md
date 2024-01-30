---
layout: page
title: common/rga (English)
description: "Ripgrep wrapper with rich file type searching capabilities."
content_hash: 9ed5374c4489003fa2091f4e15dc7560f3053ee9
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# rga

Ripgrep wrapper with rich file type searching capabilities.
More information: <https://github.com/phiresky/ripgrep-all>.

- Search recursively for a pattern in all files in the current directory:

`rga `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- List available adapters:

`rga --rga-list-adapters`

- Change which adapters to use (e.g. ffmpeg, pandoc, poppler etc.):

`rga --rga-adapters=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter1,adapter2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Search for a pattern using the mime type instead of the file extension (slower):

`rga --rga-accurate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Display help:

`rga --help`
