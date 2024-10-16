---
layout: page
title: common/exercism (한국어)
description: "문제를 다운로드하고 해결."
content_hash: 5686eb44467be31fe458c1cd94b14bc26916d6ec
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/exercism.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/exercism.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exercism

문제를 다운로드하고 해결.
더 많은 정보: <https://exercism.org/docs/using/solving-exercises/working-locally>.

- 문제에 대한 애플리케이션 토큰 및 기본 작업 공간을 구성:

`exercism configure --token=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">당신의-애플리케이션-토큰</span>` --workspace=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/선호하는/작업공간</span>

- 특정 문제를 다운로드:

`exercism download --exercise=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문제_별칭</span>` --track=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트랙_별칭</span>

- 문제 제출:

`exercism submit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 문제 해결 작업 영역의 경로를 출력:

`exercism workspace`
