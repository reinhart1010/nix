---
layout: page
title: common/steam (中文)
description: "Valve 的电子游戏平台。"
content_hash: 48bf7c52348492d978217de3df6a8b758a73b7a6
last_modified_at: 2024-06-02
related_topics:
  - title: Deutsch version
    url: /de/common/steam.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/steam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/steam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># steam

Valve 的电子游戏平台。
更多信息：<https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- 启动 Steam 同时将调试信息输出到 `stdout`:

`steam`

- 启动 Steam 并启用内置调试控制台标签页：

`steam -console`

- 在运行的 Steam 实例中启用并打开控制台标签页：

`steam steam://open/console`

- 使用指定认证信息登录 Steam:

`steam -login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- 以大屏幕模式启动 Steam:

`steam -tenfoot`

- 退出 Steam:

`steam -shutdown`
