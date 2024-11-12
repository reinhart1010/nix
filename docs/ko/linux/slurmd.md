---
layout: page
title: linux/slurmd (한국어)
description: "컴퓨트 노드에서 실행 중인 모든 작업을 모니터링하고, 작업을 수락, 실행 및 요청 시 실행 중인 작업을 종료합니다."
content_hash: 306efea27ee46c1d73e204c44aeb27c26523a0b7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/slurmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slurmd

컴퓨트 노드에서 실행 중인 모든 작업을 모니터링하고, 작업을 수락, 실행 및 요청 시 실행 중인 작업을 종료합니다.
더 많은 정보: <https://slurm.schedmd.com/slurmd.html>.

- 데몬이 재시작될 때 노드가 재부팅되었다고 보고 (테스트 목적으로 사용됨):

`slurmd -b`

- 지정된 노드명으로 데몬 실행:

`slurmd -N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드명</span>

- 지정된 파일에 로그 메시지 기록:

`slurmd -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 지정된 파일에서 설정 읽기:

`slurmd -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`slurmd -h`
