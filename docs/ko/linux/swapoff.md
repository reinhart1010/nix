---
layout: page
title: linux/swapoff (한국어)
description: "스왑을 위한 장치 및 파일 비활성화."
content_hash: 19dcdf5cba0335c0cf4a442d04f0997ec136f392
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/swapoff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swapoff

스왑을 위한 장치 및 파일 비활성화.
참고: `경로/대상/파일`은 일반 파일이나 스왑 파티션을 가리킬 수 있습니다.
더 많은 정보: <https://manned.org/swapoff>.

- 지정된 스왑 영역 비활성화:

`swapoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `/proc/swaps`의 모든 스왑 영역 비활성화:

`swapoff --all`

- 레이블로 스왑 파티션 비활성화:

`swapoff -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>
