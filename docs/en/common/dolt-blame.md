---
layout: page
title: common/dolt-blame (English)
description: "Displays commit information for each row of a Dolt table."
content_hash: 1772a8353ecc0fe1acec82cd1940cc2f7258de3d
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# dolt blame

Displays commit information for each row of a Dolt table.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-blame>.

- Display the latest commit for each row of a table:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Display the latest commits for each row of a table when the specified commit was made:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- View help:

`dolt blame --help`
