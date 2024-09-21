---
layout: page
title: common/bats (한국어)
description: "Bash 자동 테스트 시스템: Bash용 TAP (<https://testanything.org/>) 호환 테스트 프레임워크."
content_hash: b1ba2684ab65a8f59f12ab729380190b182000ae
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bats.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bats.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bats.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bats

Bash 자동 테스트 시스템: Bash용 TAP (<https://testanything.org/>) 호환 테스트 프레임워크.
더 많은 정보: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- BATS 테스트 스크립트를 실행하고 결과를 [t]AP (Test Anything Protocol) 형식으로 출력:

`bats --tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/test.bats</span>

- 테스트를 실행하지 않고 테스트 스크립트의 테스트 케이스 수([c]ount)를 계산:

`bats --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/test.bats</span>

- BATS 테스트 케이스를 반복적으로([r]ecursively) 실행 (`.bats` 확장자를 가진 파일):

`bats --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 특정 형식([F]ormat)으로 결과를 출력:

`bats --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|tap|tap13|junit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/test.bats</span>

- 테스트에 타이밍([T]iming) 정보 추가:

`bats --timing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/test.bats</span>

- 특정 개수의 작업([j]obs)을 병렬로 실행 (GNU `parallel` 을 설치해야 함):

`bats --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/test.bats</span>
