---
layout: page
title: common/umask (한국어)
description: "사용자가 새로 생성하는 파일에 대해 제한되는 읽기/쓰기/실행 권한을 관리."
content_hash: cd8433a67285b2a7ed6e093c15398cdcfa2b0b6d
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/umask.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/umask.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># umask

사용자가 새로 생성하는 파일에 대해 제한되는 읽기/쓰기/실행 권한을 관리.
더 많은 정보: <https://manned.org/umask>.

- 현재 마스크를 8진수 표기법으로 표시:

`umask`

- 현재 마스크를 기호(사람이 읽기 쉬운) 모드로 표시:

`umask -S`

- 모든 사용자에게 읽기 권한을 허용하도록 기호로 마스크 변경 (나머지 마스크 비트는 변경되지 않음):

`umask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a+r</span>

- 파일 소유자에게는 권한을 제한하지 않고, 다른 모든 사용자에게는 모든 권한을 제한하도록 마스크를 8진수로 설정:

`umask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">077</span>
