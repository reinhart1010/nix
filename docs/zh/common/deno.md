---
layout: page
title: common/deno (中文)
description: "一个安全的 JavaScript 和 TypeScript 运行时。"
content_hash: c9a86b187b7935349ee1cc450cc90385f94e4cee
last_modified_at: 2023-11-20
related_topics:
  - title: Deutsch version
    url: /de/common/deno.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/deno.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/deno.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/deno.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/deno.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/deno.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># deno

一个安全的 JavaScript 和 TypeScript 运行时。
更多信息：<https://deno.land>.

- 运行 JavaScript 或 TypeScript 文件：

`deno run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.ts</span>

- 启动 REPL（交互式 shell）：

`deno`

- 运行文件并启用网络访问：

`deno run --allow-net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.ts</span>

- 从 URL 运行文件：

`deno run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://deno.land/std/examples/welcome.ts</span>

- 从 URL 安装可执行脚本：

`deno install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://deno.land/std/examples/colors.ts</span>
