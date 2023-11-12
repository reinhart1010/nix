---
layout: page
title: common/etcd (中文)
description: "分布式，可靠的键值存储，用于分布式系统中存储最关键的数据。"
content_hash: 2181eec40ea8d2d55dbe7055a6d85c873f64aa9c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/etcd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# etcd

分布式，可靠的键值存储，用于分布式系统中存储最关键的数据。
更多信息：<https://etcd.io>.

- 启动单节点 etcd 集群：

`etcd`

- 启动一个单节点 etcd 集群，在自定义 URL 上侦听客户端请求：

`etcd --advertise-client-urls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:1234</span>` --listen-client-urls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:1234</span>

- 使用自定义名称启动单节点 etcd 集群：

`etcd --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_etcd_cluster</span>

- 启动单节点 etcd 集群，同时可以在这里看到大量监控指标 <http://localhost:2379/debug/pprof/>：

`etcd --enable-pprof --metrics extensive`
