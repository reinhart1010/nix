---
layout: page
title: linux/slurmctld (한국어)
description: "모든 다른 Slurm 데몬과 리소스를 모니터링하고 작업(잡)을 수락하며, 해당 작업에 리소스를 할당합니다."
content_hash: 74c686b9e98a248feaab5131af50abf984e47632
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/slurmctld.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slurmctld

모든 다른 Slurm 데몬과 리소스를 모니터링하고 작업(잡)을 수락하며, 해당 작업에 리소스를 할당합니다.
더 많은 정보: <https://slurm.schedmd.com/slurmctld.html>.

- 마지막 체크포인트에서 이전 `slurmctld` 상태를 모두 지우기:

`slurmctld -c`

- 데몬의 우선순위 값을 지정된 값으로 설정 (일반적으로 음수):

`slurmctld -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 지정된 파일에 로그 메시지 기록:

`slurmctld -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 도움말 표시:

`slurmctld -h`

- 버전 표시:

`slurmctld -V`
