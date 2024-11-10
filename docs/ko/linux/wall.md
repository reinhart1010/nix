---
layout: page
title: linux/wall (한국어)
description: "현재 로그인된 사용자들의 터미널에 메시지를 작성합니다."
content_hash: 03632afafee271ba672491e93f1bac9e54466dd5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wall.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/wall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wall

현재 로그인된 사용자들의 터미널에 메시지를 작성합니다.
더 많은 정보: <https://manned.org/wall>.

- 메시지 보내기:

`wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- 특정 그룹에 속한 사용자들에게 메시지 보내기:

`wall --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>

- 파일에서 메시지 보내기:

`wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 타임아웃과 함께 메시지 보내기 (기본값 300초):

`wall --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>
