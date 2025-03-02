---
layout: page
title: common/javap (中文)
description: "反汇编类文件并列出它们。"
content_hash: 6ffd47d5f952bb18dff714b4b74399e28f82b0ae
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/javap.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/javap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javap

反汇编类文件并列出它们。
更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/javap.html>.

- 反汇编并列出一个或多个 `.class` 文件：

`javap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/file1.class 路径/到/file2.class ...</span>

- 反汇编并列出一个内置类文件：

`javap java.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类</span>

- 显示帮助信息：

`javap -help`

- 显示版本信息：

`javap -version`
