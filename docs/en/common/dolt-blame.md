---
layout: page
title: common/dolt-blame (English)
description: "Display commit information for each row of a Dolt table."
content_hash: 815bdf92f287f8e118483656dbd2e335a83ac865
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# dolt blame

Display commit information for each row of a Dolt table.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-blame>.

- Display the latest commit for each row of a table:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Display the latest commits for each row of a table when the specified commit was made:

`dolt blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Display help:

`dolt blame --help`
