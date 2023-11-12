---
layout: page
title: common/cradle-sql (English)
description: "Manage Cradle SQL databases."
content_hash: c87bb811bc779e4004b1a7e27ed66b183dffee56
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# cradle sql

Manage Cradle SQL databases.
More information: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Rebuild the database schema:

`cradle sql build`

- Rebuild the database schema for a specific package:

`cradle sql build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Empty the entire database:

`cradle sql flush`

- Empty the database tables for a specific package:

`cradle sql flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Populate the tables for all packages:

`cradle sql populate`

- Populate the tables for a specific package:

`cradle sql populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
