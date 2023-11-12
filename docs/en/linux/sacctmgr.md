---
layout: page
title: linux/sacctmgr (English)
description: "View, setup, and manage Slurm accounts."
content_hash: 5901fe9f72df4111c5048f02c7d8921ab81f3fd5
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/sacctmgr.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Show details of user/association/cluster/account using a specific format:

`sacctmgr show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|association|cluster|account</span>` format="Account%10" format="GrpTRES%30"`
