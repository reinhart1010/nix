---
layout: page
title: common/http-server (한국어)
description: "정적 파일을 제공하는 간단한 정적 HTTP 서버."
content_hash: b7636ca8c86d3734260e2a54a93200f9abcf6f51
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/http-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# http-server

정적 파일을 제공하는 간단한 정적 HTTP 서버.
더 많은 정보: <https://github.com/http-party/http-server>.

- 현재 디렉터리를 제공하기 위해 기본 포트에서 수신 대기하는 HTTP 서버를 시작:

`http-server`

- 특정 디렉터리를 제공하려면 특정 포트에서 HTTP 서버를 시작:

`http-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 기본 인증을 사용하여 HTTP 서버를 시작:

`http-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 디렉토리 목록이 비활성화된 상태에서 HTTP 서버를 시작:

`http-server -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">false</span>

- 지정된 인증서를 사용하여 기본 포트에서 HTTPS 서버를 시작:

`http-server --ssl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.pem</span>

- HTTP 서버를 시작하고 출력 로깅에 클라이언트의 IP 주소를 포함:

`http-server --log-ip`

- 모든 응답에 `Access-Control-Allow-Origin: *` 헤더를 포함하여 CORS가 활성화된 HTTP 서버를 시작:

`http-server --cors`

- 로깅이 비활성화된 상태에서 HTTP 서버를 시작:

`http-server --silent`
