---
layout: page
title: linux/fprintd-enroll (한국어)
description: "지문을 데이터베이스에 등록합니다."
content_hash: 93d82fc5d96af99445ddace150646a2fdfd209f1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fprintd-enroll.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fprintd-enroll

지문을 데이터베이스에 등록합니다.
더 많은 정보: <https://manned.org/fprintd-enroll>.

- 현재 사용자의 오른손 검지 지문 등록:

`fprintd-enroll`

- 현재 사용자의 특정 손가락 지문 등록:

`fprintd-enroll --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">왼쪽-엄지|왼쪽-검지|왼쪽-중지|왼쪽-약지|왼쪽-새끼|오른쪽-엄지|오른쪽-검지|오른쪽-중지|오른쪽-약지|오른쪽-새끼</span>

- 특정 사용자의 오른손 검지 지문 등록:

`fprintd-enroll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자의 특정 손가락 지문 등록:

`fprintd-enroll --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">손가락_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 도움말 표시:

`fprintd-enroll --help`
