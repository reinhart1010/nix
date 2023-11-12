---
layout: page
title: common/etcd (English)
description: "A distributed, reliable key-value store for the most critical data of a distributed system."
content_hash: 66bfd1c56263b50aff619152700c93a4c40fca88
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/etcd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# etcd

A distributed, reliable key-value store for the most critical data of a distributed system.
More information: <https://etcd.io>.

- Start a single-node etcd cluster:

`etcd`

- Start a single-node etcd cluster, listening for client requests on a custom URL:

`etcd --advertise-client-urls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:1234</span>` --listen-client-urls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:1234</span>

- Start a single-node etcd cluster with a custom name:

`etcd --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_etcd_cluster</span>

- Start a single-node etcd cluster with extensive metrics available at <http://localhost:2379/debug/pprof/>:

`etcd --enable-pprof --metrics extensive`
