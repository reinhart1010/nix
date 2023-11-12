---
layout: page
title: common/pwsh (English)
description: "Command-line shell and scripting language designed especially for system administration."
content_hash: 463f75b92a7513be457103ba4ec92e234c5e7703
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pwsh

Command-line shell and scripting language designed especially for system administration.
This command refers to PowerShell version 6 and above (also known as PowerShell Core and cross-platform PowerShell). To use the original Windows version (5.1 and below, also known as the legacy Windows PowerShell), use `powershell` instead of `pwsh`.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Start an interactive shell session:

`pwsh`

- Start an interactive shell session without loading startup configs:

`pwsh -NoProfile`

- Execute specific commands:

`pwsh -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell is executed'</span>`"`

- Execute a specific script:

`pwsh -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.ps1</span>

- Start a session with a specific version of PowerShell:

`pwsh -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Prevent a shell from exit after running startup commands:

`pwsh -NoExit`

- Describe the format of data sent to PowerShell:

`pwsh -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Determine how an output from PowerShell is formatted:

`pwsh -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
