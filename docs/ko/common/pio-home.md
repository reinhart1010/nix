---
layout: page
title: common/pio-home (한국어)
description: "PlatformIO Home 웹 서버 시작."
content_hash: 455ef2b092f46468343e0d7a1d7b18e09ef1db21
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-home.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-home.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio home

PlatformIO Home 웹 서버 시작.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- 기본 웹 브라우저에서 PlatformIO Home 열기:

`pio home`

- 특정 HTTP 포트 사용 (기본값은 8008):

`pio home --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 IP 주소에 바인딩 (기본값은 127.0.0.1):

`pio home --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>

- 기본 웹 브라우저에서 PlatformIO Home을 자동으로 열지 않음:

`pio home --no-open`

- 클라이언트가 연결되어 있지 않을 때 타임아웃(초) 후 서버 자동 종료:

`pio home --shutdown-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>

- 고유한 세션 식별자를 지정하여 PlatformIO Home을 다른 인스턴스와 격리하고 제3자 접근으로부터 보호:

`pio home --session-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_아이디</span>
