---
layout: page
title: common/aircrack-ng (中文)
description: "破解捕获数据包中的握手时段的 WEP 和 WPA/WPA2 密钥。"
content_hash: f1868c207d4d43e5f4426e5ed970079db95a0678
last_modified_at: 2024-07-08
related_topics:
  - title: Deutsch version
    url: /de/common/aircrack-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aircrack-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aircrack-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aircrack-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aircrack-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aircrack-ng

破解捕获数据包中的握手时段的 WEP 和 WPA/WPA2 密钥。
是 Aircrack-ng 网络软件套件的一部分。
更多信息： <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- 使用字典文件破解捕获文件中的密钥：

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/字典文件.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>

- 使用字典文件和接入点的 ESSID 破解捕获文件中的密钥：

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/字典文件.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>

- 使用字典文件和接入点的 MAC 地址破解捕获文件中的密钥：

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/字典文件.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>
