---
layout: page
title: linux/sacctmgr (中文)
description: "查看、配置、管理 Slurm 账户。"
content_hash: 4f2ffcf30347fc5799e4870778a3fce467a6be42
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/sacctmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sacctmgr

查看、配置、管理 Slurm 账户。
更多信息：<https://slurm.schedmd.com/sacctmgr.html>.

- 显示现有配置：

`sacctmgr show configuration`

- 向 Slurm 数据库添加集群：

`sacctmgr add cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">集群名</span>

- 向 Slurm 数据库添加账户：

`sacctmgr add account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">账户名</span>` cluster=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">账户所在集群</span>

- 以指定格式显示用户、账户资源关联、集群、账户的详细信息：

`sacctmgr show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|association|cluster|account</span>` format="Account%10" format="GrpTRES%30"`
