---
layout: page
title: common/psalm (한국어)
description: "PHP 애플리케이션에서 오류를 찾기 위한 정적 분석 도구."
content_hash: 7246c99337bdef4117b0f7f29cb03046ed06e316
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/psalm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/psalm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/psalm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># psalm

PHP 애플리케이션에서 오류를 찾기 위한 정적 분석 도구.
더 많은 정보: <https://psalm.dev>.

- Psalm 구성 생성:

`psalm --init`

- 현재 작업 디렉터리 분석:

`psalm`

- 특정 디렉터리나 파일 분석:

`psalm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 특정 구성 파일을 사용하여 프로젝트 분석:

`psalm --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/psalm.xml</span>

- 출력에 정보성 결과 포함:

`psalm --show-info`

- 프로젝트를 분석하고 통계 표시:

`psalm --stats`

- 4개의 스레드로 병렬 프로젝트 분석:

`psalm --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
