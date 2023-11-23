---
layout: page
title: windows/powershell (English)
description: "Command-line shell and scripting language designed especially for system administration."
content_hash: f83694d3ffe8d11c0cf76c04099275166c31265e
last_modified_at: 2023-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/powershell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># powershell

Command-line shell and scripting language designed especially for system administration.
This command refers to PowerShell version 5.1 and below (also known as the legacy Windows PowerShell). To use the newer, cross-platform version of PowerShell (also known as PowerShell Core), use `pwsh` instead of `powershell`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

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
