---
layout: page
title: linux/squeue (한국어)
description: "SLURM 스케줄러에 대기 중인 작업을 표시합니다."
content_hash: 5dfe2bc0f6e11f5bd450b0dc0b52db70a80f5982
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/squeue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# squeue

SLURM 스케줄러에 대기 중인 작업을 표시합니다.
더 많은 정보: <https://manned.org/squeue>.

- 대기열 보기:

`squeue`

- 특정 사용자에 의해 대기 중인 작업 보기:

`squeue -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 대기열을 5초마다 새로고침하여 보기:

`squeue -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 예상 시작 시간과 함께 대기열 보기:

`squeue --start`
