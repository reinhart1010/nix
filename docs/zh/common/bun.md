---
layout: page
title: common/bun (中文)
description: "JavaScript 运行时和工具箱。"
content_hash: d42c160122952be6c57c3b40fa9866497037bc3d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bun.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bun.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bun.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bun

JavaScript 运行时和工具箱。
包含打包工具、测试运行器和包管理器。
更多信息：<https://bun.sh>.

- 运行 JavaScript 文件或 `package.json` 脚本：

`bun run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|script_name</span>

- 运行单元测试：

`bun test`

- 下载并安装 `package.json` 中列为依赖项的包：

`bun install`

- 向 `package.json` 添加依赖：

`bun add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">模块名称</span>

- 从 `package.json` 删除依赖：

`bun remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">模块名称</span>

- 在当前文件夹创建新的 Bun 项目：

`bun init`

- 启动 REPL（交互式 shell）：

`bun repl`

- 升级 Bun 到最新版本：

`bun upgrade`
