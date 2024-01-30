---
layout: page
title: common/dolt-blame (English)
description: "Displays commit information for each row of a Dolt table."
content_hash: a519146ec049c1bbcd9f27edc01561002070905c
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# dolt blame

Displays commit information for each row of a Dolt table.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-blame>.

- Display the latest commit for each row of a table:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Display the latest commits for each row of a table when the specified commit was made:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Display help:

`dolt blame --help`
