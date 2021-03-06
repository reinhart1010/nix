---
layout: page
title: windows/get-filehash (中文)
description: "计算一个文件的 HASH 值。"
content_hash: 26d279fc7fc2350db8c71ef74ce96f8bbdf753fc
related_topics:
  - title: English version
    url: /en/windows/get-filehash.html
    icon: bi bi-globe
---
# Get-FileHash

计算一个文件的 HASH 值。
更多信息：<https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- 使用 SHA256 算法计算给定文件的哈希值：

`Get-FileHash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 使用指定的哈希算法计算给定文件的哈希值：

`Get-FileHash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>` -Algorithm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SHA1|SHA384|SHA256|SHA512|MD5</span>
