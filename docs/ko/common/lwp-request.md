---
layout: page
title: common/lwp-request (한국어)
description: "간단한 명령줄 HTTP 클라이언트."
content_hash: 1aadc00568f96eb2d930399b19af4759aaa696da
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lwp-request.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lwp-request

간단한 명령줄 HTTP 클라이언트.
libwww-perl로 제작되었습니다.
더 많은 정보: <https://metacpan.org/pod/lwp-request>.

- 간단한 GET 요청 만들기:

`lwp-request -m GET `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/some/path</span>

- 파일을 POST 요청으로 업로드:

`lwp-request -m POST `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/some/path</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 지정 에이전트로 요청 만들기:

`lwp-request -H 'User-Agent: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_에이전트</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">METHOD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/some/path</span>

- HTTP 인증으로 요청 만들기:

`lwp-request -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">METHOD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/some/path</span>

- 요청 헤더를 출력하며 요청 만들기:

`lwp-request -U -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">METHOD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/some/path</span>

- 응답 헤더와 상태 체인을 출력하며 요청 만들기:

`lwp-request -E -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">METHOD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/some/path</span>
