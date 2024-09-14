---
layout: page
title: common/tldr (中文)
description: "显示来自 tldr-pages 项目的命令行工具的简单帮助页面。"
content_hash: f1645fd34f4e72fc92724669a4faa62efca5f49b
last_modified_at: 2024-09-14
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr

显示来自 tldr-pages 项目的命令行工具的简单帮助页面。
注意：`--language` 和 `--list` 选项并非客户端规范所必需，但大多数客户端都实现了它们。
更多信息：<https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- 打印指定命令的 tldr 页面（提示：这就是你来到这里的方式！）：

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 打印指定子命令的 tldr 页面：

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子命令</span>

- 用指定语言打印命令的 tldr 页面（如果没有，返回英语）：

`tldr --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">语言代码</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 打印指定平台的命令的 tldr 页面：

`tldr --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 更新 tldr 页面的本地缓存：

`tldr --update`

- 列出当前平台和 `common` 的所有页面：

`tldr --list`

- 列出某个命令的所有可用子命令页面：

`tldr --list | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` | column`
