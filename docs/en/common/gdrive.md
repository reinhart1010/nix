---
layout: page
title: common/gdrive (English)
description: "Interact with Google Drive."
content_hash: f388a38782e8e70af221f5a5dcebfe2b5e1222db
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# gdrive

Interact with Google Drive.
Folder/file ID can be obtained from the Google Drive folder or ID URL.
More information: <https://github.com/gdrive-org/gdrive>.

- Upload a local path to the parent folder with the specified ID:

`gdrive upload -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_folder</span>

- Download file or directory by ID to current directory:

`gdrive download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Download to a given local path by its ID:

`gdrive download --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/folder</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Create a new revision of an ID using a given file or folder:

`gdrive update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_folder</span>
