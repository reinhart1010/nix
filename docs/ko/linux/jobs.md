---
layout: page
title: linux/jobs (한국어)
description: "현재 셸에서 실행된 프로세스에 대한 정보를 표시하는 셸 내장 명령입니다."
content_hash: 878667cfd91f363d9b4a979cd9c2c26641cc0564
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/jobs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/jobs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jobs

현재 셸에서 실행된 프로세스에 대한 정보를 표시하는 셸 내장 명령입니다.
`-l` 및 `-p`를 제외한 옵션은 `bash`에만 적용됩니다.
더 많은 정보: <https://manned.org/jobs>.

- 현재 셸에서 실행된 작업 보기:

`jobs`

- 작업과 그 프로세스 ID 나열:

`jobs -l`

- 상태가 변경된 작업에 대한 정보 표시:

`jobs -n`

- 프로세스 ID만 표시:

`jobs -p`

- 실행 중인 프로세스 표시:

`jobs -r`

- 중지된 프로세스 표시:

`jobs -s`
