---
layout: page
title: common/qc (English)
description: "Manage and execute command snippets stored in QOwnNotes notes."
content_hash: 2c46cc8a20801aa0db0d7912f8945d6736419527
last_modified_at: 2024-01-22
tldri18n_status: 2
---
# qc

Manage and execute command snippets stored in QOwnNotes notes.
See also: `qownnotes`.
More information: <https://www.qownnotes.org/getting-started/command-line-snippet-manager.html>.

- Configure the snippet manager, e.g. to set the security token from QOwnNotes:

`qc configure`

- Search and print command snippets stored in your `Commands.md` note and all your notes tagged with `commands`:

`qc search`

- Execute a snippet and show the command before executing:

`qc exec --command`

- Execute the last snippet and show the command before executing:

`qc exec --command --last`

- Switch between note folders in QOwnNotes:

`qc switch`
