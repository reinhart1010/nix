---
layout: page
title: common/zmore (English)
description: "View `gzip` compressed files with `more`."
content_hash: 4bc6f7457cf0a6403eb0d57a524eeb952c5ea8c7
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# zmore

View `gzip` compressed files with `more`.
More information: <https://manned.org/zmore>.

- Open a compressed file:

`zmore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt.gz</span>

- Display the next page of the file:

`<Space>`

- Search for a pattern in the file (press `n` to go to next match):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Exit:

`q`

- Display interactive command help:

`h`
