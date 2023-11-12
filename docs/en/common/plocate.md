---
layout: page
title: common/plocate (English)
description: "Find filenames quickly."
content_hash: a581c0522b661c3e2ce150ec3708a035b77e32c5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# plocate

Find filenames quickly.
Make sure to run `sudo updatedb` to include new files.
More information: <https://plocate.sesse.net>.

- Look for patterns in the database (recomputed periodically):

`plocate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Look for a file by its exact filename (a pattern containing no globbing characters is interpreted as `*pattern*`):

`plocate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
