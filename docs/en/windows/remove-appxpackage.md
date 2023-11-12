---
layout: page
title: windows/remove-appxpackage (English)
description: "A PowerShell utility to remove an app package from one or more user accounts."
content_hash: 2e4c74f3b2c82b1aa26c65cfeeb0d5399c8ddec1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# remove-appxpackage

A PowerShell utility to remove an app package from one or more user accounts.
More information: <https://learn.microsoft.com/powershell/module/appx/remove-appxpackage>.

- Remove an app package:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove an app package for a specific user:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -User `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove an app package for all users:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -AllUsers`

- Remove an app package but preserve it's app data:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -PreserveApplicationData`
