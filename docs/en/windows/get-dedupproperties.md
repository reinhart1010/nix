---
layout: page
title: windows/get-dedupproperties (English)
description: "Gets Data Deduplication information."
content_hash: 7b12445183ac493e9b963d2da8cc3ad6b92e4063
last_modified_at: 2024-06-08
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-dedupproperties.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-DedupProperties

Gets Data Deduplication information.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- Get Data Deduplication information of the drive:

`Get-DedupProperties -DriveLetter 'C'`

- Get Data Deduplication information of the drive using the drive label:

`Get-DedupProperties -FileSystemLabel 'Label'`

- Get Data Dedpulication information of the drive using the input object:

`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
