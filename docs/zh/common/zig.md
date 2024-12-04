---
layout: page
title: common/zig (中文)
description: "Zig 编译器和工具链。"
content_hash: 8a2c802a520559e66aae8abbf88bae67a4ca445a
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zig

Zig 编译器和工具链。
更多信息：<https://ziglang.org>.

- 编译当前目录下的项目：

`zig build`

- 编译并运行当前目录下的项目：

`zig build run`

- 初始化一个 `zig build` 应用程序：

`zig init-exe`

- 初始化一个 `zig build` 库：

`zig init-lib`

- 创建并运行一个测试构建：

`zig test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zig</span>

- 将 Zig 源码重新格式化为规范格式：

`zig fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zig</span>

- 将 Zig 用作 C 编译器：

`zig cc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.c</span>

- 将 Zig 用作 C++ 编译器：

`zig c++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.cpp</span>
