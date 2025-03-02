---
layout: page
title: common/jbang (中文)
description: "简便地创建、编辑和运行仅包含源代码的自包含 Java 程序。"
content_hash: 1a8c1fda73a68010f67147e4dc782b6fc9a28a9d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jbang.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/jbang.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jbang.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jbang

简便地创建、编辑和运行仅包含源代码的自包含 Java 程序。
此命令也有关于其子命令的文件，例如：`java`.
更多信息：<https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>.

- 初始化一个简单的 Java 类：

`jbang init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.java</span>

- 初始化一个 Java 类（用于脚本编写）：

`jbang init --template=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.java</span>

- 使用 `jshell` 在 REPL 编辑器中探索和使用脚本及其任何依赖项：

`jbang run --interactive`

- 设置一个临时项目以在 IDE 中编辑脚本：

`jbang edit --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codium|code|eclipse|idea|netbeans|gitpod</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.java</span>

- 运行 Java 代码片段（Java 9 及以后版本）：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'</span>` | jbang -`

- 运行命令行应用程序：

`jbang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数1 参数2 ...</span>

- 在用户的 `$PATH` 中安装一个脚本：

`jbang app install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.java</span>

- 安装一个特定版本的 JDK 以与 `jbang` 一起使用：

`jbang jdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>
