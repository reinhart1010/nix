---
layout: page
title: common/jdeps (한국어)
description: "Java 클래스 의존성 분석기."
content_hash: 72be534b61fa7906c22f4d1f0ae7cfc2b6a4e9fa
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jdeps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jdeps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jdeps

Java 클래스 의존성 분석기.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jdeps.html>.

- `.jar` 또는 `.class` 파일의 의존성을 분석:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.class</span>

- 특정 `.jar` 파일의 모든 의존성 요약 표시:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.jar</span>` -summary`

- `.jar` 파일의 모든 클래스 레벨 의존성 표시:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.jar</span>` -verbose`

- 분석 결과를 특정 디렉토리에 DOT 파일로 출력:

`jdeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름.jar</span>` -dotoutput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 도움말 표시:

`jdeps --help`
