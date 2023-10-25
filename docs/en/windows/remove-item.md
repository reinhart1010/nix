---
layout: page
title: windows/remove-item (English)
description: "Delete files, folders, as well as registry keys and subkeys."
content_hash: 60ced6c7858631767ce8f7005cba622aae505e4d
last_modified_at: 2023-10-25
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Remove-Item

Delete files, folders, as well as registry keys and subkeys.
This command can only be run through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- Remove specific files or registry keys (without subkeys):

`Remove-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_key1 path\to\file_or_key2 ...</span>

- Remove hidden or read-only files:

`Remove-Item -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1 path\to\file2 ...</span>

- Remove specific files or registry keys interactively prompting before each removal:

`Remove-Item -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_key1 path\to\file_or_key2 ...</span>

- Remove specific files and directories recursively (Windows 10 version 1909 or later):

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory1 path\to\file_or_directory2 ...</span>

- Remove specific Windows registry keys and all its subkeys:

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\key1 path\to\key2 ...</span>

- Perform a dry run of the deletion process:

`Remove-Item -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1 path\to\file2 ...</span>
