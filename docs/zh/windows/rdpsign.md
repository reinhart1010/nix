---
layout: page
title: windows/rdpsign (中文)
description: "用于签名远程桌面协议（RDP）文件的工具。"
content_hash: ddb021f7a92715a687d518454d3bdc6092c01e50
related_topics:
  - title: English version
    url: /en/windows/rdpsign.html
    icon: bi bi-globe
---
# rdpsign

用于签名远程桌面协议（RDP）文件的工具。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/rdpsign>.

- 为一个 RDP 文件签名：

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径.rdp</span>

- 使用一个指定的 sha256 哈希值为 RDP 文件签名：

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径.rdp</span>` /sha265 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">哈希值</span>

- 启用静默输出：

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径.rdp</span>` /q`

- 显示详细的信息、警告和状态：

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径.rdp</span>` /v`

- 在不更新文件的情况下将输出显示到标准输出来测试签名：

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径.rdp</span>` /l`
