---
layout: page
title: common/xh (한국어)
description: "친숙하고 빠른 HTTP 요청 전송 도구."
content_hash: af9d246ff065117ac6534ad6330fb0a87b54aad0
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xh

친숙하고 빠른 HTTP 요청 전송 도구.
참고: Rust로 작성된 `xh`는 `http`의 효과적인 대체 도구입니다.
같이 보기: `http`, `curl`.
더 많은 정보: <https://github.com/ducaale/xh>.

- GET 요청 전송:

`xh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>

- JSON 본문과 함께 POST 요청 전송 (키-값 쌍이 최상위 JSON 객체에 추가됨, 예: `{"name": "john", "age": 25}`):

`xh post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/post</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name=john</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">age:=25</span>

- 쿼리 매개변수를 포함한 GET 요청 전송 (예: `first_param=5&second_param=true`):

`xh get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_param==5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">second_param==true</span>

- 사용자 지정 헤더와 함께 GET 요청 전송:

`xh get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/get</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">header-name:header-value</span>

- GET 요청을 보내고 응답 본문을 파일에 저장:

`xh --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpbin.org/json</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 동등한 `curl` 명령 표시 (이 명령은 요청을 전송하지 않음):

`xh --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">curl|curl-long</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--follow --verbose get http://example.com user-agent:curl</span>
