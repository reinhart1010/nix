---
layout: page
title: common/mongod (中文)
description: "MongoDB 数据库服务器。"
content_hash: 368b2f7f0b7d7647a34c7bdc983007ceab7766cc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mongod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/mongod.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mongod

MongoDB 数据库服务器。
更多信息：<https://docs.mongodb.com/manual/reference/program/mongod>.

- 指定配置文件：

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- 指定要监听的端口：

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- 指定数据库分析级别，用于性能调优分析。 0 - 关闭，1 - 仅是记录慢速操作，2 - 全部：

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
