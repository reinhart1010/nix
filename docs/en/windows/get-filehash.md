---
layout: page
title: windows/get-filehash (English)
description: "Calculate a hash for a file."
content_hash: 8330556ba65ccedc961f74a6c498722714ce1041
last_modified_at: 2023-02-20
related_topics:
  - title: 中文 version
    url: /zh/windows/get-filehash.html
    icon: bi bi-globe
---
# Get-FileHash

Calculate a hash for a file.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Calculate a hash for a specified file using the SHA256 algorithm:

`Get-FileHash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Calculate a hash for a specified file using a specified algorithm:

`Get-FileHash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` -Algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SHA1|SHA384|SHA256|SHA512|MD5</span>
