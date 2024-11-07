---
layout: page
title: common/mh_copyright (한국어)
description: "MATLAB 또는 Octave 코드의 저작권 헤더를 조정합니다."
content_hash: 4349b6221f6cc022be3f5ce78cc88ce2a6e7fcbb
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mh_copyright.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mh_copyright.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mh_copyright

MATLAB 또는 Octave 코드의 저작권 헤더를 조정합니다.
더 많은 정보: <https://misshit.org>.

- 지정된 파일의 연도(범위)를 현재 연도로 업데이트:

`mh_copyright --primary-entity="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔티티</span>`" --update-year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1.m 경로/대상/파일_또는_디렉토리2.m ...</span>

- 모든 파일의 연도(범위)를 현재 연도로 업데이트:

`mh_copyright --primary-entity="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔티티</span>`" --update-year`
