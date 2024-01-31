---
layout: page
title: osx/defaults (中文)
description: "读取和写入 macOS 应用程序的用户配置。"
content_hash: 5b0f02ba9d1f32a89fd388ab050a249753d1c42f
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/defaults.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/defaults.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># defaults

读取和写入 macOS 应用程序的用户配置。
更多信息：<https://keith.github.io/xcode-man-pages/defaults.1.html>.

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
