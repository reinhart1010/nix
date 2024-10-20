---
layout: page
title: linux/bluetoothd (中文)
description: "管理蓝牙设备的守护进程。"
content_hash: c072e0b24940761283416a9513682e5e94ffa97b
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/linux/bluetoothd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluetoothd

管理蓝牙设备的守护进程。
更多信息：<https://manned.org/bluetoothd>.

- 启动守护进程：

`bluetoothd`

- 启动守护进程，日志输出到标准输出：

`bluetoothd --nodetach`

- 指定一个配置文件启动守护进程（默认是 `/etc/bluetooth/main.conf`）：

`bluetoothd --configfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件</span>

- 启动守护进程并将详细信息输出到标准错误：

`bluetoothd --debug`

- 使用来自 bluetoothd 或插件源中特定文件启动守护进程并输出详细信息：

`bluetoothd --debug=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件一:文件二:...</span>
