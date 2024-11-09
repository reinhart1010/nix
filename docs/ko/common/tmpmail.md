---
layout: page
title: common/tmpmail (한국어)
description: "터미널에서 바로 사용할 수 있는 POSIX sh로 작성된 임시 이메일."
content_hash: 74950d7c2492176772503aad337a0e80e2646408
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tmpmail.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tmpmail.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tmpmail

터미널에서 바로 사용할 수 있는 POSIX sh로 작성된 임시 이메일.
더 많은 정보: <https://github.com/sdushantha/tmpmail>.

- 임시 받은 편지함 생성:

`tmpmail --generate`

- 메시지와 그 숫자 ID 나열:

`tmpmail`

- 가장 최근에 받은 이메일 표시:

`tmpmail --recent`

- 특정 메시지 열기:

`tmpmail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일_ID</span>

- HTML 태그 없이 이메일을 원시 텍스트로 보기:

`tmpmail --text`

- 특정 브라우저로 이메일 열기 (기본값은 w3m):

`tmpmail --browser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브라우저</span>
