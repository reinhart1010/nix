---
layout: page
title: linux/extrepo (한국어)
description: "외부 Debian 저장소 관리."
content_hash: 60e8f912d066f5d720c98f212e43cef50ae83e81
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/extrepo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# extrepo

외부 Debian 저장소 관리.
Debian에서 외부 저장소를 관리하는 데 사용됩니다.
더 많은 정보: <https://manned.org/extrepo.1p>.

- 특정 패키지 검색:

`extrepo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 저장소 활성화:

`sudo extrepo enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 저장소 비활성화:

`sudo extrepo disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>

- 저장소 업데이트:

`sudo extrepo update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>
