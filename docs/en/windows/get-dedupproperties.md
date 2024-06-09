---
layout: page
title: windows/get-dedupproperties (English)
description: "Gets Data Deduplication information."
content_hash: 7b12445183ac493e9b963d2da8cc3ad6b92e4063
last_modified_at: 2024-06-09
tldri18n_status: 2
---
# Get-DedupProperties

Gets Data Deduplication information.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- Get Data Deduplication information of the drive:

`Get-DedupProperties -DriveLetter 'C'`

- Get Data Deduplication information of the drive using the drive label:

`Get-DedupProperties -FileSystemLabel 'Label'`

- Get Data Dedpulication information of the drive using the input object:

`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
