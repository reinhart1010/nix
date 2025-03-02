---
layout: page
title: common/npm (中文)
description: "JavaScript 和 Node.js 包管理器。"
content_hash: 3ca959ec754769f208158c8e4fd77699fc381c1e
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/npm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

JavaScript 和 Node.js 包管理器。
管理 Node.js 项目及其模块依赖项。
更多信息：<https://www.npmjs.com>.

- 使用默认值创建一个 `package.json` 文件（省略 `--yes` 以交互方式执行）：

`npm init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-y|--yes</span>

- 下载 `package.json` 中列出的所有依赖项包：

`npm install`

- 下载包的特定版本并将其添加到 `package.json` 中的依赖项列表中：

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 下载包的最新版本并将其添加到 `package.json` 中的开发依赖项列表中：

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- 下载包的最新版本并全局安装：

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 卸载包并将其从 `package.json` 中的依赖项列表中删除：

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 列出所有本地安装的依赖项：

`npm list`

- 列出所有顶级全局安装的包：

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
