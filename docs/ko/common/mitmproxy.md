---
layout: page
title: common/mitmproxy (한국어)
description: "대화형 중간자 HTTP 프록시."
content_hash: 14f953b0542a0cb5d50cfbd533b319b542d0750d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mitmproxy.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mitmproxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mitmproxy

대화형 중간자 HTTP 프록시.
같이 보기: `mitmweb` 및 `mitmdump`.
더 많은 정보: <https://docs.mitmproxy.org/stable/>.

- 기본 설정으로 `mitmproxy` 시작 (포트 `8080`에서 대기):

`mitmproxy`

- 사용자 정의 주소와 포트에 바인딩하여 `mitmproxy` 시작:

`mitmproxy --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--listen-port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 스크립트를 사용하여 트래픽을 처리하는 `mitmproxy` 시작:

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scripts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/script.py</span>

- SSL/TLS 마스터 키로 로그를 외부 프로그램(와이어샤크 등)으로 내보내기:

`SSLKEYLOGFILE="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`" mitmproxy`

- 프록시 서버의 작동 모드 지정 (`regular`가 기본값):

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--mode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular|transparent|socks5|...</span>

- 콘솔 레이아웃 설정:

`mitmproxy --console-layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horizontal|single|vertical</span>
