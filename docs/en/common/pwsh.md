---
layout: page
title: common/pwsh (English)
description: "PowerShell Core is a cross-platform automation and configuration tool/framework."
content_hash: 39ca5c44525c064c7cb5c475f161ab3ea834e562
---
# pwsh

PowerShell Core is a cross-platform automation and configuration tool/framework.
More information: <https://learn.microsoft.com/powershell/>.

- Start an instance of PowerShell:

`pwsh`

- Execute a script and then exit:

`pwsh -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ps1</span>

- Set the execution policy for the current session:

`pwsh -ExecutionPolicy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AllSigned|Bypass|Default|RemoteSigned|Restricted|Undefined|Unrestricted</span>

- Execute a command and then exit:

`pwsh -Command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
