---
layout: page
title: linux/chat (한국어)
description: "모뎀 또는 시리얼 장치와의 대화를 자동화합니다."
content_hash: 627c36c94dd030d2c5c325b29d17d3350b3cbd75
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/chat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chat

모뎀 또는 시리얼 장치와의 대화를 자동화합니다.
주로 PPP(Point-to-Point Protocol) 연결을 설정하는 데 사용됩니다.
더 많은 정보: <https://manned.org/chat.8>.

- 명령줄에서 채팅 스크립트를 직접 실행:

`chat '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기대_발신_쌍</span>`'`

- 파일에서 채팅 스크립트 실행:

`chat -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/채팅_스크립트</span>`'`

- 응답을 기대하는 사용자 정의 시간 초과 설정(초 단위):

`chat -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간_초</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기대_발신_쌍</span>`'`

- 대화를 `syslog`에 기록하기 위해 자세한 출력 활성화:

`chat -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기대_발신_쌍</span>`'`

- 대화 중 수신된 특정 문자열을 기록하기 위해 보고서 파일 사용:

`chat -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/보고서_파일</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기대_발신_쌍</span>`'`

- 스크립트에서 `\T`를 대체하여 전화번호 걸기:

`chat -T '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전화번호</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"ATDT\\T CONNECT"</span>`'`

- 특정 문자열을 수신하면 중단 조건 포함:

`chat 'ABORT "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오류_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기대_발신_쌍</span>`'`
