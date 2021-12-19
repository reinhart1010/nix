---
layout: page
title: linux/cgcreate (English)
description: "Create cgroups, used to limit, measure, and control resources used by processes."
content_hash: 29b7da33506de8c27818a1afda33a2fc157e98c2
---
# cgcreate

Create cgroups, used to limit, measure, and control resources used by processes.
`cgroups` types can be `memory`, `cpu`, `net_cls`, etc.
More information: <https://manned.org/cgcreate>.

- Create a new group:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Create a new group with multiple cgroup types:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Create a subgroup:

`mkdir /sys/fs/cgroup/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subgroup_name</span>
