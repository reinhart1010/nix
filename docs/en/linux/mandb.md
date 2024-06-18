---
layout: page
title: linux/mandb (English)
description: "Manage the pre-formatted manual page database."
content_hash: 52ebc1cc3f5dfc12f8957de592b8a0af2072bf71
last_modified_at: 2024-06-18
tldri18n_status: 2
---
# mandb

Manage the pre-formatted manual page database.
More information: <https://manned.org/mandb>.

- Purge and process manual pages:

`mandb`

- Update a single entry:

`mandb --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create entries from scratch instead of updating:

`mandb --create`

- Only process user databases:

`mandb --user-db`

- Do not purge obsolete entries:

`mandb --no-purge`

- Check the validity of manual pages:

`mandb --test`
