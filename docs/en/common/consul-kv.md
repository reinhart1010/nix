---
layout: page
title: common/consul-kv (English)
description: "Distributed key-value store with health checking and service discovery."
content_hash: 95379444a63bfd856131e57ea8607ef0f74cb32c
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/consul-kv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/consul-kv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# consul-kv

Distributed key-value store with health checking and service discovery.
More information: <https://learn.hashicorp.com/consul/getting-started/kv>.

- Read a value from the key-value store:

`consul kv get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>

- Store a new key-value pair:

`consul kv put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Delete a key-value pair:

`consul kv delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>
