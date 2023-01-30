---
layout: page
title: common/pwsh (English)
description: "PowerShell Core is a cross-platform automation and configuration tool/framework."
content_hash: b3eb47947c174c278eb0b5260617e2938022db64
last_modified_at: 2023-01-30
---
# pwsh

PowerShell Core is a cross-platform automation and configuration tool/framework.
See also: `powershell`.
More information: <https://learn.microsoft.com/powershell/>.

- Start an interactive shell session:

`pwsh`

- Start an interactive shell session without loading startup configs:

`pwsh -NoProfile`

- Execute specific commands:

`pwsh -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`"`

- Execute a specific script:

`pwsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.ps1</span>

- Start an interactive shell session with a specific execution policy:

`pwsh -ExecutionPolicy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AllSigned|Bypass|Default|RemoteSigned|Restricted|...</span>
