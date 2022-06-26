---
layout: page
title: common/rip (English)
description: "Remove files or directories by sending them to the graveyard, allowing for them to be recovered."
content_hash: 975950473670c0e0c646a5ebf9e5f653d952162d
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rip

Remove files or directories by sending them to the graveyard, allowing for them to be recovered.
More information: <https://github.com/nivekuil/rip>.

- Remove files or directories from specified locations and place them in the graveyard:

`rip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/another/file_or_directory</span>

- Interactively remove files or directories, with a prompt before every removal:

`rip --inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/another/file_or_directory</span>

- List all files and directories in the graveyard that were originally within the current directory:

`rip --seance`

- Permanently delete every file and directory in the graveyard:

`rip --decompose`

- Put back the files and directories which were affected by the most recent removal:

`rip --unbury`

- Put back every file and directory that is listed by `rip --seance`:

`rip --seance --unbury`
