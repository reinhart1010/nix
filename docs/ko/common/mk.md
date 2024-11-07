---
layout: page
title: common/mk (한국어)
description: "Mkfile에 설명된 대상을 위한 태스크 실행기."
content_hash: 83b2d0b6efceb090e9af8b1601d9e0dca8494ebd
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mk

Mkfile에 설명된 대상을 위한 태스크 실행기.
주로 소스 코드에서 실행 파일의 컴파일을 제어하는 데 사용됩니다.
더 많은 정보: <https://doc.cat-v.org/plan_9/4th_edition/papers/mk>.

- Mkfile에 지정된 첫 번째 대상 호출 (일반적으로 "all"로 명명됨):

`mk`

- 특정 대상 호출:

`mk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 특정 대상 호출, 동시에 4개의 작업을 병렬로 실행:

`NPROC=4 mk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 소스 파일이 변경되지 않았더라도 대상을 강제로 만들기:

`mk -w`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 모든 대상을 최신 상태가 아닌 것으로 가정하고, `대상` 및 모든 의존성을 업데이트:

`mk -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 오류가 발생해도 가능한 한 계속 진행:

`mk -k`
