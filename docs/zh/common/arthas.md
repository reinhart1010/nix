---
layout: page
title: common/arthas (中文)
description: "Java 应用诊断利器。"
content_hash: d858ab130ba34fb939c921925ac2293b6881086e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/arthas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arthas

Java 应用诊断利器。
另见 `arthas-watch`, `arthas-trace`.
更多信息：<https://arthas.aliyun.com/en/>.

- 启动 arthas：

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/arthas-boot.jar</span>

- 重连 arthas （默认 3658 端口）：

`telnet localhost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口号</span>

- 退出当前 arthas 客户端的连接，但不停止 arthas 服务：

`exit|quit|logout|q`

- 停止 arthas 服务，断开所有 arthas 客户端的连接：

`stop`
