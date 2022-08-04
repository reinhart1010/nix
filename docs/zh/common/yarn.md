---
layout: page
title: common/yarn (中文)
description: "JavaScript 和 Node.js package manager 的一个替代。"
content_hash: 7a0fcbe6b3eb2667cee3830527e1c08a924649ce
related_topics:
  - title: English version
    url: /en/common/yarn.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/yarn.html
    icon: bi bi-globe
---
# yarn

JavaScript 和 Node.js package manager 的一个替代。
更多信息：<https://yarnpkg.com>.

- 全局安装一个模块：

`yarn global add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- 安装 `package.json` 中指定的依赖（`install` 命令是可选的 -- 你可以直接输入`yarn`）：

`yarn install`

- 安装一个模块并将其写入 `package.json` 中的依赖项（增加 `--dev` 来作为开发依赖写入）：

`yarn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- 卸载一个模块并将其从 `package.json` 的依赖项中移除：

`yarn remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- 交互式地创建一个 `package.json` 文件：

`yarn init`

- 确认一个模块是否是一个依赖项并且列出依赖其的模块：

`yarn why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>
