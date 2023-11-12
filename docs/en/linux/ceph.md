---
layout: page
title: linux/ceph (English)
description: "A unified storage system."
content_hash: eaebc0c93c8e0657ab9ac1c34799eaef9d58bdac
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ceph

A unified storage system.
More information: <https://ceph.io>.

- Check cluster health status:

`ceph status`

- Check cluster usage stats:

`ceph df`

- Get the statistics for the placement groups in a cluster:

`ceph pg dump --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain</span>

- Create a storage pool:

`ceph osd pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_number</span>

- Delete a storage pool:

`ceph osd pool delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>

- Rename a storage pool:

`ceph osd pool rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_name</span>

- Self-repair pool storage:

`ceph pg repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pool_name</span>
