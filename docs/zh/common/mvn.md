---
layout: page
title: common/mvn (中文)
description: "Apache Maven."
content_hash: 0a82692899927934fd7f96ab7e30e8934213705a
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/mvn.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mvn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mvn

Apache Maven.
用于构建和管理基于 Java 的项目的工具。
更多信息：<https://maven.apache.org>.

- 编译项目：

`mvn compile`

- 将编译后的代码打包成可分发格式，比如 `jar`：

`mvn package`

- 编译和打包，跳过单元测试：

`mvn package -DskipTests`

- 在本地 maven 存储库中安装构建的包（这也会调用 compile 和 package 命令）：

`mvn install`

- 从目标目录中删除构建工件，通常用来清理之前的编译结果：

`mvn clean`

- 执行清理操作，然后进行编译打包：

`mvn clean package`

- 清理然后使用给定的构建配置文件打包代码：

`mvn clean -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">构建配置</span>` package`

- 使用 main 方法运行一个类：

`mvn exec:java -Dexec.mainClass="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.Main</span>`" -Dexec.args="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数1 参数2</span>`"`
