---
layout: page
title: osx/xctool (中文)
description: "用于构建 Xcode 项目的工具。"
content_hash: f6526be6e69b69640371a68541ec236e5d6ab5d9
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/osx/xctool.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xctool.html
    icon: bi bi-globe
---
# xctool

用于构建 Xcode 项目的工具。
更多信息：<https://github.com/facebookarchive/xctool>.

- 在没有任何工作区的情况下生成单个项目：

`xctool -project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你的项目.名称</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">方案</span>` build`

- 构建属于工作区的项目：

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你的工作区.名字</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">方案</span>` build`

- 清理、构建和执行所有测试：

`xctool -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">你的工作区.名字</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">方案</span>` clean build test`
