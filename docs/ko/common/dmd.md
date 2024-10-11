---
layout: page
title: common/dmd (한국어)
description: "공식적 D 컴파일러."
content_hash: d94ce7143d8fd0ef6fea158ab2dc6e0c232f2e84
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/dmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dmd

공식적 D 컴파일러.
더 많은 정보: <https://dlang.org/dmd.html>.

- D 소스 파일 빌드:

`dmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.d</span>

- 모든 템플릿 인스턴스화에 대한 코드 생성:

`dmd -allinst`

- 제어 범위 확인:

`dmd -boundscheck=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|safeonly|off</span>

- 사용 가능한 모든 체크사항에 대한 나열:

`dmd -check=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|help|?</span>

- 색깔있는 콘솔 출력을 보여줌:

`dmd -color`
