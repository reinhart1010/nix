---
layout: page
title: linux/datamash (한국어)
description: "입력 텍스트 데이터 파일에 대해 기본적인 수치, 텍스트 및 통계 작업 수행."
content_hash: 93b526aaa59f4d35c76df1af132cf8a882d2395c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/datamash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/datamash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># datamash

입력 텍스트 데이터 파일에 대해 기본적인 수치, 텍스트 및 통계 작업 수행.
더 많은 정보: <https://www.gnu.org/software/datamash/>.

- 한 열의 숫자에 대한 최대값, 최소값, 평균 및 중앙값 계산:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- 부동 소수점 숫자(소수점은 ","로 표시)를 포함한 한 열의 평균 계산:

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- 지정된 소수 자릿수로 한 열의 숫자 평균 계산:

`echo -e '1\n2\n3\n4\n5\n5' | datamash -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원하는_소수_자릿수</span>` mean 1`

- "Na"와 "NaN"(문자열)을 무시하고 한 열의 숫자 평균 계산:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
