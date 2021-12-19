---
layout: page
title: common/jenv (中文)
description: "管理”JAVA_HOME“环境变量的命令行工具。"
content_hash: 2985ddb7b0c20ffce2c0504fca546cab782f5a9b
related_topics:
  - title: English version
    url: /en/common/jenv.html
    icon: bi bi-globe
---
# jenv

管理”JAVA_HOME“环境变量的命令行工具。
更多信息：<https://www.jenv.be/>.

- 向 jEnv 添加一个 Java 版本：

`jenv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java Home 路径</span>

- 显示当前使用的 JDK 版本：

`jenv version`

- 显示所有托管的 JDK：

`jenv versions`

- 设置全局JDK版本：

`jenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 版本</span>

- 设置当前 shell 会话的 JDK 版本：

`jenv shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Java 版本</span>

- 启用 jEnv 插件：

`jenv enable-plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">插件名称</span>
