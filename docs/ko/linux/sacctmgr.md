---
layout: page
title: linux/sacctmgr (한국어)
description: "Slurm 계정을 조회, 설정 및 관리."
content_hash: 79bef10e851377d74ca0e235f85e27ab238d2f59
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sacctmgr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sacctmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sacctmgr

Slurm 계정을 조회, 설정 및 관리.
더 많은 정보: <https://slurm.schedmd.com/sacctmgr.html>.

- 현재 구성 보기:

`sacctmgr show configuration`

- Slurm 데이터베이스에 클러스터 추가:

`sacctmgr add cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- Slurm 데이터베이스에 계정 추가:

`sacctmgr add account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_이름</span>` cluster=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정의_클러스터</span>

- 특정 형식을 사용하여 사용자/연관/클러스터/계정 세부 정보 보기:

`sacctmgr show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|association|cluster|account</span>` format="Account%10" format="GrpTRES%30"`
