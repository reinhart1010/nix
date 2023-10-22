---
layout: page
title: windows/remove-appxpackage (English)
description: "A PowerShell utility to remove an app package from one or more user accounts."
content_hash: b4f8a592f7f8a12bb9b0cdd3299c86e3eb9b6333
last_modified_at: 2023-10-22
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># remove-appxpackage

A PowerShell utility to remove an app package from one or more user accounts.
More information: <https://learn.microsoft.com/en-us/powershell/module/appx/remove-appxpackage>.

- Remove an app package:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Remove an app package for a specific user:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -User `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Remove an app package for all users:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -AllUsers`

- Remove an app package but preserve it's app data:

`remove-appxpackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` -PreserveApplicationData`
