---
layout: page
title: common/pgmhist (한국어)
description: "PGM 이미지에 포함된 값의 히스토그램을 출력."
content_hash: 0b8f604f12879bb7d00d02989b97b74c78dc39fb
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/pgmhist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pgmhist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pgmhist

PGM 이미지에 포함된 값의 히스토그램을 출력.
같이 보기: `ppmhist`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmhist.html>.

- 사람이 읽을 수 있는 히스토그램 표시:

`pgmhist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>

- 중간 회색 값 표시:

`pgmhist -median `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>

- 네 개의 사분위수 회색 값 표시:

`pgmhist -quartile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>

- 잘못된 회색 값의 존재 여부 보고:

`pgmhist -forensic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>

- 기계가 읽을 수 있는 출력 표시:

`pgmhist -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>
