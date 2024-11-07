---
layout: page
title: common/lli (한국어)
description: "LLVM 비트코드에서 프로그램을 직접 실행."
content_hash: eec6aa3e89f7dd3cab68a5c1d571bf162951f5c2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lli

LLVM 비트코드에서 프로그램을 직접 실행.
더 많은 정보: <https://www.llvm.org/docs/CommandGuide/lli.html>.

- 비트코드 또는 IR 파일 실행:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ll</span>

- 명령줄 인수와 함께 실행:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 모든 최적화 활성화:

`lli -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ll</span>

- 링크 전에 동적 라이브러리 로드:

`lli --dlopen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ll</span>
