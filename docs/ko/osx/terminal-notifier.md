---
layout: page
title: osx/terminal-notifier (한국어)
description: "macOS 사용자 알림을 전송합니다."
content_hash: 6fd89f9616bf77dcaa0e6d6dd69426e5ef8e3afe
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/terminal-notifier.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/terminal-notifier.html
    icon: bi bi-globe
tldri18n_status: 2
---
# terminal-notifier

macOS 사용자 알림을 전송합니다.
더 많은 정보: <https://github.com/julienXX/terminal-notifier>.

- 알림 전송 (메시지만 필수):

`terminal-notifier -group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-info</span>` -title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR</span>` -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TLDR rocks</span>`'`

- 소리와 함께 파이프로 전달된 데이터 표시:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파이프로 전달된 메시지 데이터!</span>`' | terminal-notifier -sound `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default</span>

- 알림을 클릭하면 URL 열기:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Apple 주식을 확인하세요!</span>`' -open '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://finance.yahoo.com/q?s=AAPL</span>`'`

- 알림을 클릭하면 앱 열기:

`terminal-notifier -message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42개의 연락처를 가져왔습니다.</span>`' -activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.AddressBook</span>
