---
layout: page
title: linux/strigger (English)
description: "View or modify Slurm trigger information."
content_hash: 8444d7579740d055aabb07685aa5768c46407383
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# strigger

View or modify Slurm trigger information.
Triggers are actions that are automatically run when an event occurs on a Slurm cluster.
More information: <https://slurm.schedmd.com/strigger.html>.

- Register a new trigger. Execute the specified program when the specified event occurs:

`strigger --set --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...</span>` --program=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>

- Execute the specified program when the specified job terminated:

`strigger --set --jobid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` --fini --program="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>`"`

- View active triggers:

`strigger --get`

- View active triggers regarding the specified job:

`strigger --get --jobid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Clear the specified trigger:

`strigger --clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger_id</span>
