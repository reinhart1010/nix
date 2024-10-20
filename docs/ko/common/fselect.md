---
layout: page
title: common/fselect (한국어)
description: "SQL과 유사한 쿼리로 파일을 찾음."
content_hash: d9c1424dfa3031f9fb22ef42ef304ef55e84996d
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fselect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fselect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fselect

SQL과 유사한 쿼리로 파일을 찾음.
더 많은 정보: <https://github.com/jhspetersson/fselect>.

- 특정 디렉터리의 임시 또는 구성 파일에서 전체 경로와 크기를 선택:

`fselect size, path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` where name = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*.cfg'</span>` or name = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*.tmp'</span>

- 정사각형 이미지 찾기:

`fselect path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` where width = height`

- 옛날 랩 320kbps MP3 파일 찾기:

`fselect path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` where genre = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rap</span>` and bitrate = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">320</span>` and mp3_year lt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>

- 처음 5개 결과만 선택하고 JSON으로 출력:

`fselect size, path from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` into json`

- SQL 집계 함수를 사용하여, 디렉터리에 있는 파일의 최소, 최대 및 평균 크기를 계산:

`fselect "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)</span>` from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>`"`
