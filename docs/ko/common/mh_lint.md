---
layout: page
title: common/mh_lint (한국어)
description: "MATLAB 또는 Octave 코드에서 버그를 찾으려 시도합니다."
content_hash: f99aa452ab558a9f88493b5732636020721ddf98
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mh_lint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mh_lint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mh_lint

MATLAB 또는 Octave 코드에서 버그를 찾으려 시도합니다.
이 도구는 완벽하지도 않고 완전하지도 않음을 유의하세요.
더 많은 정보: <https://misshit.org>.

- 현재 디렉토리 검사:

`mh_lint`

- 특정 디렉토리를 재귀적으로 검사:

`mh_lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- MATLAB 파일 검사:

`mh_lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.m</span>

- Octave 파일 검사:

`mh_lint --octave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.m</span>
