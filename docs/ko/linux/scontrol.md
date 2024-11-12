---
layout: page
title: linux/scontrol (한국어)
description: "작업에 대한 정보를 보고 수정합니다."
content_hash: 00003a3dbd8ad0cd95ca31cfbd45c106ccd1d3e7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/scontrol.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scontrol

작업에 대한 정보를 보고 수정합니다.
더 많은 정보: <https://slurm.schedmd.com/scontrol.html>.

- 작업에 대한 정보 표시:

`scontrol show job `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 쉼표로 구분된 실행 중인 작업 목록 일시 중지:

`scontrol suspend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID1,작업_ID2,...</span>

- 쉼표로 구분된 일시 중지된 작업 목록 재개:

`scontrol resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID1,작업_ID2,...</span>

- 쉼표로 구분된 대기 중인 작업 목록 보류 (작업 예약을 허용하려면 `release` 명령 사용):

`scontrol hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID1,작업_ID2,...</span>

- 쉼표로 구분된 일시 중지된 작업 목록 해제:

`scontrol release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID1,작업_ID2,...</span>
