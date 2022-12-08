---
layout: page
title: common/trash-cli (English)
description: "A command-line interface to the trashcan APIs."
content_hash: f0aaa5c7e3312ee87947b897ff14d478a3fff4bc
last_modified_at: 2022-12-08
---
# trash-cli

A command-line interface to the trashcan APIs.
More information: <https://github.com/andreafrancia/trash-cli>.

- Trash specific files and directories into the current trashcan:

`trash-put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Remove specific files from the current trashcan:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Empty the current trashcan:

`trash-empty`

- List trashed files and directories in the current trashcan:

`trash-list`

- Restore a specific file or directory by a number from the displayed list from the current trashcan:

`trash-restore`
