---
layout: page
title: common/xzmore (한국어)
description: "`xz` 또는 `lzma`로 압축된 파일의 텍스트를 표시."
content_hash: 8e0ab1163e6a72be0b07bc7c0dd24dfa60466c74
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xzmore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzmore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzmore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzmore

`xz` 또는 `lzma`로 압축된 파일의 텍스트를 표시.
`xzless`와 거의 동일하지만, `PAGER` 환경 변수를 존중하고 기본적으로 `more`를 사용하며, 페이지 매개변수에 옵션을 전달할 수 없습니다.
더 많은 정보: <https://manned.org/xzmore>.

- 압축된 파일 보기:

`xzmore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
