---
layout: page
title: windows/set-location (English)
description: "Display the current working directory or move to a different directory."
content_hash: 9a1ee0cb3e751131653a7d3fb3b45a7f17b4b839
last_modified_at: 2024-06-07
related_topics:
  - title: Indonesia version
    url: /id/windows/set-location.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/set-location.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Set-Location

Display the current working directory or move to a different directory.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Go to the specified directory:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Go to a specific directory in a different drive:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Go and display the location of specified directory:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` -PassThru`

- Go up to the parent of the current directory:

`Set-Location ..`

- Go to the home directory of the current user:

`Set-Location ~`

- Go back/forward to the previously chosen directory:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-|+</span>

- Go to root of current drive:

`Set-Location \`
