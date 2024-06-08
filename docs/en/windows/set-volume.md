---
layout: page
title: windows/set-volume (English)
description: "Sets or changes the file system label of an existing volume."
content_hash: 6a8921406169f4b3f1c19f73291ee27f4ebfcb4a
last_modified_at: 2024-06-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/set-volume.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Set-Volume

Sets or changes the file system label of an existing volume.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/storage/set-volume>.

- Change the file system label of a volume identified by drive letter:

`Set-Volume -DriveLetter "D" -NewFileSystemLabel "DataVolume"`

- Change the file system label of a volume identified by the system label:

`Set-Volume -FileSystemLabel "OldLabel" -NewFileSystemLabel "NewLabel"`

- Modify the properties of a volume using a volume object:

`Set-Volume -InputObject $(Get-Volume -DriveLetter "E") -NewFileSystemLabel "Backup"`

- Specify the Data Deduplication mode for the volume:

`Set-Volume -DriveLetter "D" -DedupMode Backup`
