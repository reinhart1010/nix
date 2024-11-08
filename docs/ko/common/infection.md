---
layout: page
title: common/infection (한국어)
description: "PHP용 코드 변경 테스팅 프레임워크."
content_hash: 3e0b213ddbdd9e664d49706c91955ef6108d978b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/infection.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/infection.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># infection

PHP용 코드 변경 테스팅 프레임워크.
더 많은 정보: <https://infection.github.io>.

- 구성 파일을 사용하여 코드를 분석 (또는 존재하지 않는 경우 새롭게 생성):

`infection`

- 특정 수의 스레드를 사용:

`infection --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스레드_수</span>

- 최소 MSI(Mutation Score Indicator)를 지정:

`infection --min-msi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백분율</span>

- 최소 적용 코드 MSI를 지정:

`infection --min-covered-msi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백분율</span>

- 특정 테스트 프레임워크를 사용 (기본값은 PHPUnit):

`infection --test-framework `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">phpunit|phpspec</span>

- 테스트에 포함된 코드 줄만 변경:

`infection --only-covered`

- 적용된 코드 변경을 주는 부분을 표시:

`infection --show-mutations`

- 로그 상세 수준을 지정:

`infection --log-verbosity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default|all|none</span>
