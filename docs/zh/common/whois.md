---
layout: page
title: common/whois (中文)
description: "WHOIS（RFC 3912）协议的命令行客户端。"
content_hash: 099f95efa64e62068704bf52d14fbd4089725ff9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/whois.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whois

WHOIS（RFC 3912）协议的命令行客户端。
更多信息：<https://github.com/rfc1036/whois>.

- 获取域名信息：

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 获取 IP 地址信息：

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- 获取 IP 地址用于报告滥用的联系方式：

`whois -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>
