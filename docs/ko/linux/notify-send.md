---
layout: page
title: linux/notify-send (한국어)
description: "현재 데스크톱 환경의 알림 시스템을 사용하여 알림을 생성합니다."
content_hash: 7b14307b0033abcea726a7607e361577f176ddc6
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/notify-send.html
    icon: bi bi-globe
tldri18n_status: 2
---
# notify-send

현재 데스크톱 환경의 알림 시스템을 사용하여 알림을 생성합니다.
더 많은 정보: <https://manned.org/notify-send>.

- 제목 "Test"와 내용 "This is a test"로 알림 표시:

`notify-send "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">This is a test</span>`"`

- 사용자 지정 아이콘과 함께 알림 표시:

`notify-send -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이콘.png</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이것은 테스트입니다</span>`"`

- 5초 동안 알림 표시:

`notify-send -t 5000 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이것은 테스트입니다</span>`"`

- 앱의 아이콘과 이름으로 알림 표시:

`notify-send "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Test</span>`" --icon=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google-chrome</span>` --app-name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Google Chrome</span>`"`
