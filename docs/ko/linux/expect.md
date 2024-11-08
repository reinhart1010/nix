---
layout: page
title: linux/expect (한국어)
description: "사용자 입력이 필요한 다른 프로그램과 상호작용하는 스크립트 실행기."
content_hash: b0299ad8e5c37a3bca3a49d39b52a5626cb0755d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/expect.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/expect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/expect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># expect

사용자 입력이 필요한 다른 프로그램과 상호작용하는 스크립트 실행기.
더 많은 정보: <https://manned.org/expect>.

- 파일에서 expect 스크립트 실행:

`expect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 expect 스크립트 실행:

`expect -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어들</span>`"`

- 대화형 REPL 모드로 진입 (`exit` 또는 Ctrl + D로 종료):

`expect -i`
