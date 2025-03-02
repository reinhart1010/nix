---
layout: page
title: common/unlink (中文)
description: "从文件系统中删除对文件的链接。"
content_hash: 555b893ac6f866b2c562e89b641f31fb084a3390
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/unlink.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unlink.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unlink.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unlink

从文件系统中删除对文件的链接。
如果链接是文件的最后一个，文件内容将丢失。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/unlink-invocation.html>.

- 如果是最后一个链接，则删除指定的文件：

`unlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
