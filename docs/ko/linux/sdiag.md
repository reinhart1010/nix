---
layout: page
title: linux/sdiag (한국어)
description: "`slurmctld` 실행에 대한 정보를 표시합니다."
content_hash: f309817daa36bed90d645f8c76c917708d34af1f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sdiag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sdiag

`slurmctld` 실행에 대한 정보를 표시합니다.
더 많은 정보: <https://slurm.schedmd.com/sdiag.html>.

- `slurmctld` 실행과 관련된 모든 성능 카운터 표시:

`sdiag --all`

- `slurmctld` 실행과 관련된 성능 카운터 재설정:

`sdiag --reset`

- 출력 형식 지정:

`sdiag --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|yaml</span>

- 명령을 보낼 클러스터 지정:

`sdiag --all --cluster=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>
