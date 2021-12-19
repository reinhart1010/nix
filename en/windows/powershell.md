---
layout: page
title: windows/powershell (English)
description: "Command-line shell and scripting language designed especially for system administration."
content_hash: 067d77e0c36d705d11f6a204dccb6e9c65f9b455
related_topics:
  - title: 中文 version
    url: /zh/windows/powershell.html
    icon: bi bi-globe
---
# powershell

Command-line shell and scripting language designed especially for system administration.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start a Windows PowerShell session in a Command Prompt window:

`powershell`

- Load a specific PowerShell console file:

`powershell -PSConsoleFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start a session with a specified version of PowerShell:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Prevent the shell from exit after running startup commands:

`powershell -NoExit`

- Describe the format of data sent to PowerShell:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Determine how output from PowerShell is formatted:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Display help:

`powershell -Help`
