---
layout: page
title: common/nu (한국어)
description: "Nushell(\"새로운 유형의 셸\")은 명령줄에 대한 현대적이고 구조화된 접근 방식을 제공합니다."
content_hash: 6dc05f1f4beb7cc3d0941fc06f03db5acbf95e20
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nu

Nushell("새로운 유형의 셸")은 명령줄에 대한 현대적이고 구조화된 접근 방식을 제공합니다.
같이 보기: `elvish`.
더 많은 정보: <https://www.nushell.sh>.

- 대화형 셸 세션 시작:

`nu`

- 특정 명령 실행:

`nu --commands "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'nu is executed'</span>`"`

- 특정 스크립트 실행:

`nu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.nu</span>

- 로깅을 포함하여 특정 스크립트 실행:

`nu --log-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warn|info|debug|trace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.nu</span>
