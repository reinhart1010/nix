---
layout: page
title: osx/networksetup (中文)
description: "网络系统首选项配置工具。"
content_hash: 6ba32ce7ac24b641572a32ff4a92b4eff36024dd
related_topics:
  - title: English version
    url: /en/osx/networksetup.html
    icon: bi bi-globe
---
# networksetup

网络系统首选项配置工具。
更多信息：<https://support.apple.com/guide/remote-desktop/about-networksetup-apdd0c5a2d5/mac>.

- 列出可用的网络服务源（以太网、Wi-Fi、蓝牙等）：

`networksetup -listallnetworkservices`

- 显示特定网络设备的配置信息：

`networksetup -getinfo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Wi-Fi</span>`"`

- 获取当前连接的 Wi-Fi 网络名称（Wi-Fi 设备通常为 en0 或 en1）：

`networksetup -getairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>

- 连接到给定的 Wi-Fi 网络 Connect to a particular Wi-Fi network：

`networksetup -setairportnetwork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">无线网 SSID</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>
