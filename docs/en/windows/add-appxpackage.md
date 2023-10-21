---
layout: page
title: windows/add-appxpackage (English)
description: "A PowerShell utility to add a signed app package (`.appx`, `.msix`, `.appxbundle` and `.msixbundle`) to a user account."
content_hash: 5b1e0ab6ac88c540878963fa5e19d336c7c2a8a4
last_modified_at: 2023-10-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># add-appxpackage

A PowerShell utility to add a signed app package (`.appx`, `.msix`, `.appxbundle` and `.msixbundle`) to a user account.
More information: <https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage>.

- Add an app package:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\package.msix</span>

- Add an app package with dependencies:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\package.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\dependencies.msix</span>

- Install an app using the app installer file:

`add-appxpackage -AppInstallerFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\app.appinstaller</span>

- Add an unsigned package:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\package.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\dependencies.msix</span>` -AllowUnsigned`
