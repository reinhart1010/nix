---
layout: page
title: linux/strigger (한국어)
description: "Slurm 트리거 정보를 조회하거나 수정합니다."
content_hash: 6d0ffa0c7e3755cbd46939ce1d60b995eae82194
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/strigger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# strigger

Slurm 트리거 정보를 조회하거나 수정합니다.
트리거는 Slurm 클러스터에서 이벤트가 발생할 때 자동으로 실행되는 작업입니다.
더 많은 정보: <https://slurm.schedmd.com/strigger.html>.

- 새로운 트리거 등록: 지정된 이벤트가 발생할 때 지정된 프로그램을 실행:

`strigger --set --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...</span>` --program=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- 지정된 작업이 종료될 때 지정된 프로그램을 실행:

`strigger --set --jobid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` --fini --program="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>`"`

- 활성 트리거 보기:

`strigger --get`

- 지정된 작업과 관련된 활성 트리거 보기:

`strigger --get --jobid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 지정된 트리거 삭제:

`strigger --clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트리거_ID</span>
