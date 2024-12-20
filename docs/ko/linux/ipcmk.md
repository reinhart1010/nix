---
layout: page
title: linux/ipcmk (한국어)
description: "IPC(프로세스 간 통신) 리소스 생성."
content_hash: ecebc30a30e772fee9a19f95cb3fb1c7215a7d3c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ipcmk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipcmk

IPC(프로세스 간 통신) 리소스 생성.
더 많은 정보: <https://manned.org/ipcmk>.

- 공유 메모리 세그먼트 생성:

`ipcmk --shmem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세그먼트_크기_바이트</span>

- 세마포어 생성:

`ipcmk --semaphore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">요소_크기</span>

- 메시지 큐 생성:

`ipcmk --queue`

- 특정 권한으로 공유 메모리 세그먼트 생성 (기본값은 0644):

`ipcmk --shmem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세그먼트_크기_바이트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8진수_권한</span>
