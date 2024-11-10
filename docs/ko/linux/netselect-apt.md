---
layout: page
title: linux/netselect-apt (한국어)
description: "지연 시간이 가장 낮은 Debian 미러를 위한 `sources.list` 파일 생성."
content_hash: 163f5de72f47ae1ebd94bb1d0edb0dd27d3a289d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/netselect-apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netselect-apt

지연 시간이 가장 낮은 Debian 미러를 위한 `sources.list` 파일 생성.
더 많은 정보: <https://manned.org/netselect-apt>.

- 가장 낮은 지연 시간의 서버를 사용하여 `sources.list` 생성:

`sudo netselect-apt`

- Debian 브랜치를 지정, 기본적으로 stable이 사용됨:

`sudo netselect-apt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testing</span>

- non-free 섹션 포함:

`sudo netselect-apt --non-free`

- 미러 목록 조회를 위한 국가 지정:

`sudo netselect-apt -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인도</span>
