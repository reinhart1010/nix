---
layout: page
title: linux/sacctmgr (中文)
description: "查看、配置、管理 Slurm 账户。"
content_hash: 41c3c7c6b6ad71e9e6f576a03f470864e479f2d2
related_topics:
  - title: English version
    url: /en/linux/sacctmgr.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sacctmgr

查看、配置、管理 Slurm 账户。
更多信息：<https://slurm.schedmd.com/sacctmgr.html>。

- 显示现有配置：

`sacctmgr show configuration`

- 向 Slurm 数据库添加集群：

`sacctmgr add cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">集群名</span>

- 向 Slurm 数据库添加账户：

`sacctmgr add account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">账户名</span>` cluster=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">账户所在集群</span>

- 以指定格式显示用户、账户资源关联、集群、账户的详细信息：

`sacctmgr show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|association|cluster|account</span>` format="Accout%10" format="GrpTRES%30"`
