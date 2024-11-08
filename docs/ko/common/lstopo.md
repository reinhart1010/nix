---
layout: page
title: common/lstopo (한국어)
description: "시스템의 하드웨어 토폴로지를 보여줍니다."
content_hash: dbdd00c65fc7cc301153327874487130e5380a8c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lstopo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/lstopo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lstopo

시스템의 하드웨어 토폴로지를 보여줍니다.
더 많은 정보: <https://manned.org/lstopo>.

- 그래픽 창에서 요약된 시스템 토폴로지 표시 (그래픽 디스플레이가 없는 경우 콘솔에 출력):

`lstopo`

- 요약 없이 전체 시스템 토폴로지 표시:

`lstopo --no-factorize`

- 요약된 시스템 토폴로지를 [p]hysical 인덱스만 사용하여 표시 (즉, OS에서 보는 것처럼):

`lstopo --physical`

- 지정된 형식으로 파일에 전체 시스템 토폴로지 작성:

`lstopo --no-factorize --output-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">콘솔|ascii|tex|fig|svg|pdf|ps|png|xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 단색 또는 회색조로 출력:

`lstopo --palette `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">없음|회색</span>
