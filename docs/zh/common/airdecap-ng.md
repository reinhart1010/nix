---
layout: page
title: common/airdecap-ng (中文)
description: "解密 WEP、WPA 或 WPA2 加密的捕获文件。"
content_hash: 4e2cb5a97b3f0a0546e643602fff1b470a9eddf6
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/common/airdecap-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airdecap-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airdecap-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airdecap-ng

解密 WEP、WPA 或 WPA2 加密的捕获文件。
是 Aircrack-ng 网络软件套件的一部分。
更多信息： <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- 从开放网络捕获文件中移除无线头，并使用接入点的 MAC 地址进行过滤：

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>

- 使用十六进制格式的密钥解密 WEP 加密的捕获文件：

`airdecap-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>

- 使用接入点的 ESSID 和密码解密 WPA/WPA2 加密的捕获文件：

`airdecap-ng -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>

- 使用接入点的 ESSID 和密码解密 WPA/WPA2 加密的捕获文件，并保留头部信息：

`airdecap-ng -l -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>

- 使用接入点的 MAC 地址进行过滤，并使用接入点的 ESSID 和密码解密 WPA/WPA2 加密的捕获文件：

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/捕获文件.cap</span>
