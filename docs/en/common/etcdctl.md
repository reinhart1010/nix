---
layout: page
title: common/etcdctl (English)
description: "Interact with `etcd`, a highly-available key-value pair store."
content_hash: f12aafb96e5c8afa422a4e17fdcf111a38294179
last_modified_at: 2023-07-16
---
# etcdctl

Interact with `etcd`, a highly-available key-value pair store.
More information: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- Display the value associated with a specified key:

`etcdctl get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my/key</span>

- Store a key-value pair:

`etcdctl put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my/key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_value</span>

- Delete a key-value pair:

`etcdctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my/key</span>

- Store a key-value pair, reading the value from a file:

`etcdctl put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my/file</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Save a snapshot of the etcd keystore:

`etcdctl snapshot save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/snapshot.db</span>

- Restore a snapshot of an etcd keystore (restart the etcd server afterwards):

`etcdctl snapshot restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/snapshot.db</span>

- Add a user:

`etcdctl user add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_user</span>

- Watch a key for changes:

`etcdctl watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my/key</span>
