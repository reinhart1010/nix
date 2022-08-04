---
layout: page
title: common/nomad (English)
description: "Distributed, highly available, datacenter-aware scheduler."
content_hash: 0bb3924254a4aa7daf9e47ae97e6109351bc2215
---
# nomad

Distributed, highly available, datacenter-aware scheduler.
More information: <https://www.nomadproject.io/docs/commands/>.

- Show the status of nodes in the cluster:

`nomad node status`

- Validate a job file:

`nomad job validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nomad</span>

- Plan a job for execution on the cluster:

`nomad job plan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nomad</span>

- Run a job on the cluster:

`nomad job run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.nomad</span>

- Show the status of jobs currently running on the cluster:

`nomad job status`

- Show the detailed status information about a specific job:

`nomad job status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_name</span>

- Follow the logs of a specific allocation:

`nomad alloc logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alloc_id</span>

- Show the status of storage volumes:

`nomad volume status`
