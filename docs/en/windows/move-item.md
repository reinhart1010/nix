---
layout: page
title: windows/move-item (English)
description: "Move or rename files, directories, registry keys, and other PowerShell data items."
content_hash: 009ecaea0f0e6afaf4f7ec365cad44c99bd8a220
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Move-Item

Move or rename files, directories, registry keys, and other PowerShell data items.
This command can only be run through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- Rename a file or directory when the target is not an existing directory:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\target</span>

- Move a file or directory into an existing directory:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\existing_directory</span>

- Rename or move file(s) with specific name (do not treat special characters inside strings):

`Move-Item -LiteralPath "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>

- Move multiple files into an existing directory, keeping the filenames unchanged:

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source1 , path\to\source2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\existing_directory</span>

- Move or rename registry key(s):

`Move-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_key1 , path\to\source_key2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\new_or_existing_key</span>

- Do not prompt for confirmation before overwriting existing files or registry keys:

`mv -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\target</span>

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`mv -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\target</span>

- Move files in dry-run mode, showing files and directories which could be moved without executing them:

`mv -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\target</span>
