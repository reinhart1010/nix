---
layout: page
title: osx/systemsetup (中文)
description: "配置系统首选项计算机设置。"
content_hash: dd9bf64e6908675dc6b5782b653457c18a405a9d
related_topics:
  - title: English version
    url: /en/osx/systemsetup.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/systemsetup.html
    icon: bi bi-globe
---
# systemsetup

配置系统首选项计算机设置。
更多信息：<https://ss64.com/osx/systemsetup.html>.

- 启用远程登录（SSH）：

`systemsetup -setremotelogin on`

- 指定时区、NTP 服务器并启用网络时间：

`systemsetup -settimezone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">美国 / 太平洋</span>` -setnetworktimeserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us.pool.ntp.org</span>` -setusingnetworktime on`

- 使机器从不休眠，并在电源故障或内核死机时自动重新启动：

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- disks 选择启动：

`systemsetup -liststartupdisks`

- 指定新的启动盘：

`systemsetup -setstartupdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径</span>
