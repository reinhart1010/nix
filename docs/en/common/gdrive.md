---
layout: page
title: common/gdrive (English)
description: "Command-line tool to interact with Google Drive."
content_hash: 6da28896a31031dd455a3e16c1783a472243a03a
---
# gdrive

Command-line tool to interact with Google Drive.
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
