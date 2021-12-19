---
layout: page
title: common/babel (中文)
description: "一款 JavaScript 的编译器，将下一代 ES 语法转换为兼容语法。"
content_hash: 16685b19a7186f792425ac7aa6e7d0e2bd4fdb42
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/babel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/babel.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/babel.html
    icon: bi bi-globe
---
# babel

一款 JavaScript 的编译器，将下一代 ES 语法转换为兼容语法。
更多信息：<https://babeljs.io/>.

- 转编译指定文件到标准输出：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 转编译指定文件，输入为特定文件：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件</span>

- 监听文件变动触发转编译：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` --watch`

- 转编译整个目录下的 js 文件：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件目录</span>

- 跳过指定目录下指定文件的编译（多文件使用英文逗号“,”分隔）：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件目录</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">被忽略文件</span>

- 转编译后，执行压缩：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` --minified`

- 使用预设值：

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">预设项</span>

- 输出所有可用的选项：

`babel --help`
