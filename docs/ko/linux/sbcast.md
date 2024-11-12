---
layout: page
title: linux/sbcast (한국어)
description: "작업에 할당된 노드로 파일 전송."
content_hash: 85c6331694f6296f43bea90bf667179421071214
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sbcast.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sbcast

작업에 할당된 노드로 파일 전송.
이 명령은 Slurm 배치 작업 내에서만 사용해야 합니다.
더 많은 정보: <https://slurm.schedmd.com/sbcast.html>.

- 현재 작업에 할당된 모든 노드로 파일 전송:

`sbcast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>

- 전송하는 파일이 의존하는 공유 라이브러리를 자동으로 감지하여 함께 전송:

`sbcast --send-libs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적지</span>
