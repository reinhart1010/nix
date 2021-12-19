---
layout: page
title: osx/defaults (中文)
description: "读取和写入 macOS 应用程序的用户配置。"
content_hash: 849ef2183988a3ac63a04e97a80a15671dc0c535
related_topics:
  - title: English version
    url: /en/osx/defaults.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/defaults.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># defaults

读取和写入 macOS 应用程序的用户配置。
更多信息：<https://ss64.com/osx/defaults.html>.

- 读取应用程序选项的系统默认值：

`defaults read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">选项</span>

- 读取应用程序选项的默认值：

`defaults read -app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">选项</span>

- 写入应用程序选项的默认值：

`defaults write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">选项</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">- 类型</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 加速任务控制界面弹出动画（时间设置为 0.1）：

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- 删除应用程序的所有默认值：

`defaults delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>
