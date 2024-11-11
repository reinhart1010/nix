---
layout: page
title: linux/swaks (한국어)
description: "스위스 아미 나이프 SMTP, 다목적 SMTP 트랜잭션 테스터."
content_hash: 2023f395daa889d7f403fb5ca532d3b0ad06bb5c
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/swaks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/swaks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swaks

스위스 아미 나이프 SMTP, 다목적 SMTP 트랜잭션 테스터.
더 많은 정보: <https://github.com/jetmore/swaks/blob/develop/doc/base.pod>.

- `test-server.example.net`의 포트 25에 `user@example.com`으로 표준 테스트 이메일 전송:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test-server.example.net</span>

- 사용자 `me@example.com`으로 CRAM-MD5 인증을 요구하며 표준 테스트 이메일 전송. 이메일 본문에 "X-Test" 헤더 추가:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>` --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CRAM-MD5</span>` --auth-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me@example.com</span>` --header-X-Test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_email</span>`"`

- 첨부 파일로 EICAR을 사용하여 바이러스 스캐너 테스트. 메시지 DATA 부분은 표시하지 않음:

`swaks -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --attach - --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test-server.example.com</span>` --suppress-data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/eicar.txt</span>

- 이메일 본문에 GTUBE를 사용하여 스팸 스캐너 테스트, `example.com`의 MX 레코드를 통해 라우팅:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/gtube_파일</span>

- UNIX 도메인 소켓 파일을 통해 LMTP 프로토콜을 사용하여 `user@example.com`으로 표준 테스트 이메일 전송:

`swaks --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>` --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/var/lda.sock</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LMTP</span>
