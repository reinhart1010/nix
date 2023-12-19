---
layout: page
title: linux/sh5util (English)
description: "Merge HDF5 files produced by the `sacct_gather_profile` plugin."
content_hash: 3f59adfccd6766fa11e5a8aa08c36916c7b808f0
last_modified_at: 2023-12-19
tldri18n_status: 2
---
# sh5util

Merge HDF5 files produced by the `sacct_gather_profile` plugin.
More information: <https://slurm.schedmd.com/sh5util.html>.

- Merge HDF5 files produced on each allocated node for the specified job or step:

`sh5util --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id|job_id.step_id</span>

- Extract one or more data series from a merged job file:

`sh5util --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id|job_id.step_id</span>` --extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.h5</span>` --series=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Energy|Filesystem|Network|Task</span>

- Extract one data item from all nodes in a merged job file:

`sh5util --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id|job_id.step_id</span>` --item-extract --series=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Energy|Filesystem|Network|Task</span>` --data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_item</span>
