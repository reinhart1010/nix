---
layout: page
title: common/uuencode (한국어)
description: "바이너리 파일을 ASCII로 인코딩하여 단순 ASCII 인코딩만 지원하는 매체를 통해 전송."
content_hash: d604ec9b40b497f9a0062b6e334aa99bfcbcbb72
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/uuencode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uuencode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uuencode

바이너리 파일을 ASCII로 인코딩하여 단순 ASCII 인코딩만 지원하는 매체를 통해 전송.
더 많은 정보: <https://manned.org/uuencode>.

- 파일을 인코딩하여 `stdout`에 결과 출력:

`uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디코딩_후_출력_파일_이름</span>

- 파일을 인코딩하여 결과를 파일에 저장:

`uuencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디코딩_후_출력_파일_이름</span>

- 기본 uuencode 인코딩 대신 Base64를 사용하여 파일을 인코딩하고 결과를 파일에 저장:

`uuencode -m -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디코딩_후_출력_파일_이름</span>
