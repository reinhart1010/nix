---
layout: page
title: windows/psversiontable (English)
description: "A read-only variable (as `$PSVersionTable`) to get the current PowerShell version."
content_hash: 38d71bb49668d517b6eab4427150282b68a12c2d
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# PSVersionTable

A read-only variable (as `$PSVersionTable`) to get the current PowerShell version.
This command can only be run under PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_automatic_variables#psversiontable>.

- Print a summary of the currently installed PowerShell version and edition:

`$PSVersionTable`

- Get the detailed (major, minor, build, and revision) version number of PowerShell:

`$PSVersionTable.PSVersion`

- List all supported PowerShell script versions that this PowerShell version supports:

`$PSVersionTable.PSCompatibleVersions`

- Get the latest Git commit ID where the currently-installed PowerShell version is based on (works on PowerShell 6.0 and later):

`$PSVersionTable.GitCommitId`

- Check whether the user is running PowerShell Core (6.0 or later) or the original "Windows PowerShell" (version 5.1 or below):

`$PSVersionTable.PSEdition`
