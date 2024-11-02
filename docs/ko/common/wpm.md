---
layout: page
title: common/wpm (한국어)
description: "타이프레이서와 유사한 콘솔 앱으로, 분당 타자 수(WPM)를 측정합니다."
content_hash: 8c76b3c55df9a4a71100f9d680dd7d886786fe3b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wpm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wpm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wpm

타이프레이서와 유사한 콘솔 앱으로, 분당 타자 수(WPM)를 측정합니다.
더 많은 정보: <https://github.com/cslarsen/wpm>.

- `wpm` 시작:

`wpm`

- 짧은 텍스트로 `wpm` 시작:

`wpm --short`

- 특정 텍스트 파일을 사용하여 `wpm` 시작:

`wpm --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 레이스 점수에 태그 지정:

`wpm --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그_이름</span>

- 태그별로 그룹화된 점수 통계 표시:

`wpm --stats`

- 단색으로 `wpm` 시작:

`wpm --monochrome`
