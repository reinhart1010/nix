---
layout: page
title: linux/swaplabel (한국어)
description: "스왑 영역의 레이블 또는 UUID를 출력하거나 변경합니다."
content_hash: 30776c992c856c8b83ca07138ee57ae60b976f18
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/swaplabel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swaplabel

스왑 영역의 레이블 또는 UUID를 출력하거나 변경합니다.
참고: `경로/대상/파일`은 일반 파일 또는 스왑 파티션을 가리킬 수 있습니다.
더 많은 정보: <https://manned.org/swaplabel>.

- 스왑 영역의 현재 레이블과 UUID 표시:

`swaplabel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 스왑 영역의 레이블 설정:

`swaplabel --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 스왑 영역의 UUID 설정 (UUID는 `uuidgen`을 사용하여 생성할 수 있습니다):

`swaplabel --uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_UUID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
