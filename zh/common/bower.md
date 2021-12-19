---
layout: page
title: common/bower (中文)
description: "前端 web 开发的包管理优化工具。"
content_hash: 9128761fa8ab0c1cfd5d8bda3657bd519a32db2a
related_topics:
  - title: English version
    url: /en/common/bower.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bower.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bower.html
    icon: bi bi-globe
---
# bower

前端 web 开发的包管理优化工具。
一个包可以是 GitHub 中 user/repo 的缩写，一个 Git 端口，一个 URL 链接或者一个已注册的包。
更多信息：<https://bower.io/>.

- 安装列在项目下 的 `bower.json` 文件中的依赖：

`bower install`

- 安装一个或者多个依赖到 `bower_components` 目录：

`bower install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名2</span>

- 从本地的 `bower_components` 目录卸载依赖：

`bower uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名2</span>

- 列出本地包和可能的更新项：

`bower list`

- 显示 bower 指令的帮助信息：

`bower help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指令</span>

- 创建你的项目的 `bower.json`:

`bower init`

- 安装时候指定依赖的版本号，并添加到 `bower.json`:

`bower install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_name</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` --save`
