---
layout: page
title: osx/codesign (中文)
description: "为 macOS 的应用程序签名。"
content_hash: 8e98a74714ef6b0f83bff0174558c2ec4215aec7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/codesign.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/codesign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# codesign

为 macOS 的应用程序签名。
更多信息：<https://www.unix.com/man-page/osx/1/codesign/>.

- 用证书签名：

`codesign -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">公司名称</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 应用名.app</span>

- 验证应用程序的签名：

`codesign -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 应用名.app</span>
