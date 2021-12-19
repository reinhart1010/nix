---
layout: page
title: linux/mandb (English)
description: "Manage the pre-formatted manual page database."
content_hash: 3ee1708a3eb9db8378ef42d941d04e91358662bf
---
# mandb

Manage the pre-formatted manual page database.
More information: <https://man7.org/linux/man-pages/man8/mandb.8.html>.

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
