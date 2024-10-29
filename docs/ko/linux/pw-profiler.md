---
layout: page
title: linux/pw-profiler (한국어)
description: "로컬 또는 원격 인스턴스를 프로파일링."
content_hash: 4b02a13a589a4dab4d8e9df920af999814ceb822
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-profiler.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-profiler.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-profiler

로컬 또는 원격 인스턴스를 프로파일링.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-profiler_1.html>.

- 기본 인스턴스를 프로파일링하고 `profile.log`에 기록 (`gnuplot` 파일과 결과 시각화를 위한 HTML 파일도 생성됨):

`pw-profiler`

- 로그 출력 파일 변경:

`pw-profiler --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>

- 원격 인스턴스를 프로파일링:

`pw-profiler --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 도움말 표시:

`pw-profiler --help`
