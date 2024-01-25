---
layout: page
title: windows/remove-appxpackage (English)
description: "A PowerShell utility to remove an app package from user accounts."
content_hash: bed6c615c8000b0804d95499a2d4c5abe615332c
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# Remove-AppxPackage

A PowerShell utility to remove an app package from user accounts.
More information: <https://learn.microsoft.com/powershell/module/appx/Remove-AppxPackage>.

- Remove an app package:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove an app package for a specific user:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -User `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove an app package for all users:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -AllUsers`

- Remove an app package but preserve it's app data:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -PreserveApplicationData`
