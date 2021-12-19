---
layout: page
title: windows/choco-outdated (中文)
description: "使用 Chocolatey 检查过时的包。"
content_hash: 9ff35c73d6bb8dbe6ae013b0b9401cb0a9ed3417
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-outdated.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-outdated.html
    icon: bi bi-globe
---
# choco outdated

使用 Chocolatey 检查过时的包。
更多信息：<https://chocolatey.org/docs/commands-outdated>.

- 用表格的形式列出过时的包：

`choco outdated`

- 忽略输出中的固定包：

`choco outdated --ignore-pinned`

- 从自定义的源处检查过时的包：

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源 URL|别名</span>

- 提供一个用户名和密码来进行验证：

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>
