---
layout: page
title: common/powershell (English)
description: "Command-line shell and scripting language designed especially for system administration."
content_hash: 9b7ce7c932ab20dec9b66b1a90dd14d0af7fd94c
---
# powershell

Command-line shell and scripting language designed especially for system administration.
See also: `pwsh`.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start an interactive shell session:

`powershell`

- Start an interactive shell session without loading startup configs:

`powershell -NoProfile`

- Execute specific commands:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell is executed'</span>`"`

- Execute a specific script:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.ps1</span>

- Start a session with a specific version of PowerShell:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Prevent a shell from exit after running startup commands:

`powershell -NoExit`

- Describe the format of data sent to PowerShell:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Determine how an output from PowerShell is formatted:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
