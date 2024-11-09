---
layout: page
title: common/shopt (한국어)
description: "Bash 셸 옵션 관리: Bash 셸에 특화된 동작을 제어하는 변수(`$BASHOPTS`에 저장)."
content_hash: ec857e257149aac144bd552d5024c9c3f68aaaef
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/shopt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shopt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shopt

Bash 셸 옵션 관리: Bash 셸에 특화된 동작을 제어하는 변수(`$BASHOPTS`에 저장).
일반적인 POSIX 셸 변수는 `set` 명령으로 대신 관리 (`$SHELLOPTS`에 저장).
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html>.

- 설정 가능한 모든 옵션과 설정 여부 나열:

`shopt`

- 옵션 설정:

`shopt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_이름</span>

- 옵션 해제:

`shopt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션_이름</span>

- 실행 가능한 `shopt` 명령으로 형식화된 모든 옵션과 상태 목록 출력:

`shopt -p`

- 도움말 표시:

`help shopt`
