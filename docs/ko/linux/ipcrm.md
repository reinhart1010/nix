---
layout: page
title: linux/ipcrm (한국어)
description: "IPC(프로세스 간 통신) 리소스를 삭제합니다."
content_hash: c7b8a60e9df38bcf93748b2dd8f9c09193383713
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ipcrm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipcrm

IPC(프로세스 간 통신) 리소스를 삭제합니다.
더 많은 정보: <https://manned.org/ipcrm>.

- ID로 공유 메모리 세그먼트 삭제:

`ipcrm --shmem-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공유_메모리_ID</span>

- 키로 공유 메모리 세그먼트 삭제:

`ipcrm --shmem-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">공유_메모리_키</span>

- ID로 IPC 큐 삭제:

`ipcrm --queue-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IPC_큐_ID</span>

- 키로 IPC 큐 삭제:

`ipcrm --queue-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IPC_큐_키</span>

- ID로 세마포어 삭제:

`ipcrm --semaphore-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세마포어_ID</span>

- 키로 세마포어 삭제:

`ipcrm --semaphore-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세마포어_키</span>

- 모든 IPC 리소스 삭제:

`ipcrm --all`
