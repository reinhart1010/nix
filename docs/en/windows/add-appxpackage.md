---
layout: page
title: windows/add-appxpackage (English)
description: "A PowerShell utility to add a signed app package (`.appx`, `.msix`, `.appxbundle` and `.msixbundle`) to a user account."
content_hash: 35b77509a52838ef432d32ccd8d056bf3556e741
last_modified_at: 2023-11-12
related_topics:
  - title: हिन्दी version
    url: /hi/windows/add-appxpackage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# add-appxpackage

A PowerShell utility to add a signed app package (`.appx`, `.msix`, `.appxbundle` and `.msixbundle`) to a user account.
More information: <https://learn.microsoft.com/powershell/module/appx/add-appxpackage>.

- Add an app package:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\package.msix</span>

- Add an app package with dependencies:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\package.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\dependencies.msix</span>

- Install an app using the app installer file:

`add-appxpackage -AppInstallerFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\app.appinstaller</span>

- Add an unsigned package:

`add-appxpackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\package.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\dependencies.msix</span>` -AllowUnsigned`
