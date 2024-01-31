---
layout: page
title: linux/snapper (English)
description: "Filesystem snapshot management tool."
content_hash: 558e81e0bd17686f734aa6939f4cfda0e43a36c6
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/snapper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snapper

Filesystem snapshot management tool.
More information: <http://snapper.io/manpages/snapper.html>.

- List snapshot configs:

`snapper list-configs`

- Create snapper config:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config</span>` create-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a snapshot with a description:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config</span>` create -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_description</span>`"`

- List snapshots for a config:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config</span>` list`

- Delete a snapshot:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config</span>` delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_number</span>

- Delete a range of snapshots:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config</span>` delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot1</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot2</span>
