---
layout: page
title: windows/driverquery (中文)
description: "显示已安装设备驱动程序的信息。"
content_hash: be6db430642d2c08988dde6564e32803172ddc10
related_topics:
  - title: English version
    url: /en/windows/driverquery.html
    icon: bi bi-globe
---
# driverquery

显示已安装设备驱动程序的信息。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- 显示所有已安装设备驱动程序的列表：

`driverquery`

- 以指定格式显示驱动程序的列表：

`driverquery /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 显示带有列的驱动程序列表，以表明它们是否已签名：

`driverquery /si`

- 排除输出列表中的标题：

`driverquery /nh`

- 显示远程计算机的驱动程序列表：

`driverquery /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 显示详细信息的驱动程序列表：

`driverquery /v`

- 显示详细的使用信息：

`driverquery /?`
