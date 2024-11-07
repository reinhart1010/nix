---
layout: page
title: common/phing (한국어)
description: "Apache Ant를 기반으로 한 PHP 빌드 도구."
content_hash: 866c1426092244ae73d918f8dcebc9691a4e1e04
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/phing.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phing.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phing

Apache Ant를 기반으로 한 PHP 빌드 도구.
더 많은 정보: <https://www.phing.info>.

- `build.xml` 파일에서 기본 태스크 수행:

`phing`

- 새 빌드 파일 초기화:

`phing -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/build.xml</span>

- 특정 태스크 수행:

`phing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태스크_이름</span>

- 지정된 빌드 파일 경로 사용:

`phing -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/build.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태스크_이름</span>

- 주어진 파일에 로그 기록:

`phing -logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태스크_이름</span>

- 빌드에서 사용자 정의 속성 사용:

`phing -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태스크_이름</span>

- 사용자 정의 리스너 클래스 지정:

`phing -listener `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태스크_이름</span>

- 자세한 출력으로 빌드:

`phing -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태스크_이름</span>
