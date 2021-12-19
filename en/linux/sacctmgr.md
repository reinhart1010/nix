---
layout: page
title: linux/sacctmgr (English)
description: "View, setup, and manage Slurm accounts."
content_hash: f1908f4927f16320d35b5faaab2a314dd4ed3527
---
# sacctmgr

View, setup, and manage Slurm accounts.
More information: <https://slurm.schedmd.com/sacctmgr.html>.

- Show current configuration:

`sacctmgr show configuration`

- Add a cluster to the slurm database:

`sacctmgr add cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>

- Add an account to the slurm database:

`sacctmgr add account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_name</span>` cluster=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_of_account</span>

- Show details of user/association/cluster/account:

`sacctmgr show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/association/cluster/account</span>
