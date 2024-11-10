---
layout: page
title: linux/fuser (한국어)
description: "파일이나 소켓을 현재 사용 중인 프로세스 ID를 표시합니다."
content_hash: 760b3cfbf8740df1b61fde2d6af26c15f15c9721
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fuser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fuser

파일이나 소켓을 현재 사용 중인 프로세스 ID를 표시합니다.
더 많은 정보: <https://manned.org/fuser>.

- 파일이나 폴더에 접근 중인 프로세스 찾기:

`fuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 더 많은 필드 표시 (`USER`, `PID`, `ACCESS`, `COMMAND`):

`fuser --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- TCP 소켓을 사용하는 프로세스 식별:

`fuser --namespace tcp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 파일이나 폴더에 접근 중인 모든 프로세스 종료 (`SIGKILL` 신호 전송):

`fuser --kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 특정 파일이나 폴더가 포함된 파일 시스템에 접근 중인 프로세스 찾기:

`fuser --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 특정 포트에서 TCP 연결을 가진 모든 프로세스 종료:

`fuser --kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>`/tcp`
