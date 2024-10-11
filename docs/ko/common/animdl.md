---
layout: page
title: common/animdl (한국어)
description: "매우 효율적으로 강력하며, 빠른 애니메이션 스크레이퍼."
content_hash: 67c8b955a306f9a5a3644c4d015e7d0493a8c853
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/animdl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/animdl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># animdl

매우 효율적으로 강력하며, 빠른 애니메이션 스크레이퍼.
참고: `ani-cli`.
더 많은 정보: <https://github.com/justfoolingaround/animdl>.

- 특정 애니메이션 다운로드:

`animdl download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>

- 에피소드 범위를 지정하여 특정 애니메이션을 다운로드:

`animdl download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--range</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_에피소드</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_에피소드</span>

- 다운로드 디렉터리를 지정하여 특정 애니메이션을 다운로드:

`animdl download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--download-dir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다운로드_디렉터리</span>

- 특정 애니메이션의 스트림 URL을 확인:

`animdl grab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>

- 다음주에 예정된 애니메이션 일정을 표시:

`animdl schedule`

- 특정 애니메이션 검색:

`animdl search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>

- 특정 애니메이션 스트리밍:

`animdl stream `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>

- 특정 애니메이션의 최신 에피소드를 스트리밍:

`animdl stream `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애니메이션_제목</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--special</span>` latest`
