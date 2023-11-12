---
layout: page
title: linux/cgexec (English)
description: "Limit, measure, and control resources used by processes."
content_hash: 9087c5b39ad8dade37685040e2c1e930a1e0f565
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cgexec

Limit, measure, and control resources used by processes.
Multiple cgroup types (aka controllers) exist, such as `cpu`, `memory`, etc.
More information: <https://manned.org/cgexec>.

- Execute a process in a given cgroup with given controller:

`cgexec -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">controller</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cgroup_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
