---
layout: page
title: common/jhsdb (中文)
description: "附加到一个 Java 进程或启动一个事后调试器来分析崩溃的 Java 虚拟机的核心转储。"
content_hash: 67dca86e4c0fa501b61e5aae0555fe64d6aeabb3
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jhsdb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jhsdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jhsdb

附加到一个 Java 进程或启动一个事后调试器来分析崩溃的 Java 虚拟机的核心转储。
更多信息：<https://manned.org/jhsdb>.

- 打印 Java 进程的堆栈和锁信息：

`jhsdb jstack --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程id</span>

- 在交互式调试模式下打开一个核心转储：

`jhsdb clhsdb --core `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/core_dump</span>` --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/jdk/bin/java</span>

- 启动远程调试服务器：

`jhsdb debugd --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程id</span>` --serverid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可选的唯一标识</span>

- 在交互式调试模式下连接到一个进程：

`jhsdb clhsdb --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程id</span>
