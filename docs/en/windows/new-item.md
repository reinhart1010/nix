---
layout: page
title: windows/new-item (English)
description: "Create a new file, directory, symbolic link, or a registry entry."
content_hash: 4d147d37841342f2eef94649b70c9cb5fc7f5278
last_modified_at: 2024-06-07
related_topics:
  - title: Nederlands version
    url: /nl/windows/new-item.html
    icon: bi bi-globe
tldri18n_status: 2
---
# New-Item

Create a new file, directory, symbolic link, or a registry entry.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- Create a new blank file (equivalent to `touch`):

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Create a new directory:

`New-Item -ItemType Directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Write a new text file with specified content:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content</span>

- Write the same text file in multiple locations:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file1 , path\to\file2 , ...</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content</span>

- Create a symbolic link\hard link\junction to a file or directory:

`New-Item -ItemType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SymbolicLink|HardLink|Junction</span>` -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\link_file</span>` -Target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\source_file_or_directory</span>

- Create a new blank registry entry (in REG_SZ, use `New-ItemProperty` or `Set-ItemProperty` to fine-tune the value type):

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\registry_key</span>

- Create a new blank registry entry with specified value:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\registry_key</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
