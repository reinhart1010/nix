---
layout: page
title: common/nxcdb (English)
description: "Interact with the NetExec database."
content_hash: d29c0f22b29d0d6dcc0bb0519518f11b5590bb18
last_modified_at: 2024-10-28
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nxcdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nxcdb

Interact with the NetExec database.
More information: <https://www.netexec.wiki/getting-started/database-general-usage>.

- Enter an interactive database session:

`nxcdb`

- Display the currently active workspace:

`nxcdb --get-workspace`

- Create a new workspace:

`nxcdb --create-workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name</span>

- Activate the specified workspace:

`nxcdb --set-workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workspace_name</span>
