---
layout: page
title: osx/codesign (中文)
description: "为 macOS 的应用程序签名。"
content_hash: e1ca272e3e905cd1d595a7010394c0c6c5af2648
last_modified_at: 2024-01-31
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
更多信息：<https://keith.github.io/xcode-man-pages/codesign.1.html>.

- 用证书签名：

`codesign --sign "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">公司名称</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 应用名.app</span>

- 验证应用程序的签名：

`codesign --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径 / 应用名.app</span>
