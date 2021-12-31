---
layout: page
title: linux/sacctmgr (English)
description: "View, setup, and manage Slurm accounts."
content_hash: 7f241beef1bb69ff5265ea13514888a74f0aec6c
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

- Show details of user/association/cluster/account using a spcific format:

`sacctmgr show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|association|cluster|account</span>` format="Accout%10" format="GrpTRES%30"`
