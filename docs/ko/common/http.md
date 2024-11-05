---
layout: page
title: common/http (한국어)
description: "HTTPie: 테스트, 디버깅 및 일반적으로 API 및 HTTP 서버와 상호작용하도록 설계된 HTTP 클라이언트."
content_hash: 982836e457ad5cda341f77e7009706dec22817db
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/http.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/http.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/http.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/http.html
    icon: bi bi-globe
tldri18n_status: 2
---
# http

HTTPie: 테스트, 디버깅 및 일반적으로 API 및 HTTP 서버와 상호작용하도록 설계된 HTTP 클라이언트.
더 많은 정보: <https://httpie.io/docs/cli/usage>.

- 간단한 GET 요청을 수행 (응답 헤더 및 콘텐츠 표시):

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.org</span>

- 특정 출력 내용을 인쇄 (`H`: 요청 헤더, `B`: 요청 본문, `h`: 응답 헤더, `b`: 응답 본문, `m`: 응답 메타데이터):

`http --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">H|B|h|b|m|Hh|Hhb|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 요청을 보낼 때 HTTP 메소드를 지정하고 프록시를 사용하여 요청을 가로채기:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|HEAD|PUT|PATCH|DELETE|...</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http|https</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080|socks5://localhost:9050|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- `3xx` 리디렉션을 따르고 요청에 추가 헤더를 지정:

`http `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-F|--follow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'User-Agent: Mozilla/5.0' 'Accept-Encoding: gzip'</span>

- 다양한 인증 방법을 사용하여 서버에 인증:

`http --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:password|token</span>` --auth-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic|digest|bearer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|POST|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/auth</span>

- 요청을 생성하지만, 보내지 않음 (모의 실행과 유사):

`http --offline `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|DELETE|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 지속적인 사용자 정의 헤더, 인증 자격 증명 및 쿠키에 대해 명명된 세션을 사용:

`http --session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름|경로/대상/세션.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--auth 사용자명:비밀번호 https://example.com/auth API-KEY:xxx</span>

- 양식에 파일을 업로드 (아래 예에서는 양식 필드가 `<input type="file" name="cv" />`라고 가정):

`http --form `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/upload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cv@경로/대상/파일</span>
