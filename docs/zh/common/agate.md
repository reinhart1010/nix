---
layout: page
title: common/agate (中文)
description: "一个简单的 Gemini 网络协议的服务器。"
content_hash: 23b57af8f89d2d18323237dd32ea9b3f93130e4c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/agate.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/agate.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/agate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/agate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/agate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/agate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agate

一个简单的 Gemini 网络协议的服务器。
更多信息：<https://github.com/mbrubeck/agate>.

- 运行并生成一个私钥和证书：

`agate --content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/内容/</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[::]:1965</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0:1965</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-US</span>

- 启动服务器：

`agate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 显示帮助：

`agate -h`
