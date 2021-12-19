---
layout: page
title: common/cradle-sql (English)
description: "Manage Cradle SQL databases."
content_hash: 75f20a91413de25e926da7b52f0b64da568eb177
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-sql.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-sql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-sql.html
    icon: bi bi-globe
---
# cradle sql

Manage Cradle SQL databases.
More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Rebuild the database schema:

`cradle sql build`

- Rebuild the database schema for a specific package:

`cradle sql build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Empty the entire database:

`cradle sql flush`

- Empty the database tables for a specific package:

`cradle sql flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Populate the tables for all packages:

`cradle sql populate`

- Populate the tables for a specific package:

`cradle sql populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
