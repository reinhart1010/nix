---
layout: page
title: linux/sstat (한국어)
description: "실행 중인 작업에 대한 정보를 표시합니다."
content_hash: cc8ffd857c5fdb16bc6c3170beaf64ad68eab291
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sstat

실행 중인 작업에 대한 정보를 표시합니다.
더 많은 정보: <https://slurm.schedmd.com/sstat.html>.

- 쉼표로 구분된 작업 목록의 상태 정보를 표시:

`sstat --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 쉼표로 구분된 작업 목록의 작업 ID, 평균 CPU 및 평균 가상 메모리 크기를 파이프로 구분하여 표시:

`sstat --parsable --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JobID,AveCPU,AveVMSize</span>

- 사용 가능한 필드 목록 표시:

`sstat --helpformat`
