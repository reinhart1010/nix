---
layout: page
title: common/rspec (한국어)
description: "Ruby 코드를 테스트하기 위한 Ruby로 작성된 행동 주도 개발 테스트 프레임워크."
content_hash: 08487516ad75d24700b18449f67dfd598237392b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rspec.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rspec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rspec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rspec

Ruby 코드를 테스트하기 위한 Ruby로 작성된 행동 주도 개발 테스트 프레임워크.
더 많은 정보: <https://rspec.info>.

- .rspec 구성 파일과 spec 헬퍼 파일 초기화:

`rspec --init`

- 모든 테스트 실행:

`rspec`

- 특정 디렉터리의 테스트 실행:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 하나 이상의 테스트 파일 실행:

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 파일 내 특정 테스트 실행 (예: 테스트가 83번째 줄에서 시작하는 경우):

`rspec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">83</span>

- 특정 시드로 스펙 실행:

`rspec --seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시드_번호</span>
