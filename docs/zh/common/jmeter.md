---
layout: page
title: common/jmeter (中文)
description: "开源的 Java 应用程序，旨在对功能行为进行负载测试并衡量性能。"
content_hash: d33de26f470dd06fb089668e9e0aff4563af22df
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jmeter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jmeter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jmeter

开源的 Java 应用程序，旨在对功能行为进行负载测试并衡量性能。
更多信息：<https://jmeter.apache.org>.

- 在非 GUI 模式下运行指定的测试计划：

`jmeter --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.jmx</span>

- 在非 GUI 模式下使用指定的日志文件运行测试计划：

`jmeter --nogui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.jmx</span>` --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/日志文件.jtl</span>

- 在非 GUI 模式下使用指定代理运行测试计划：

`jmeter --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.jmx</span>` --proxyHost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` --proxyPort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>

- 在非 GUI 模式下使用指定的 JMeter 属性运行测试计划：

`jmeter --jmeterproperty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键</span>`='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>`' --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.jmx</span>
