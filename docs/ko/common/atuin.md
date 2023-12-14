---
layout: page
title: common/atuin (한국어)
description: "검색 가능한 데이터베이스에 쉘 기록을 저장하세요."
content_hash: 3ea17be48cfe0d551dcc1c3066ec5d5f80f505c3
last_modified_at: 2023-12-14
related_topics:
  - title: English version
    url: /en/common/atuin.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atuin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atuin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atuin

검색 가능한 데이터베이스에 쉘 기록을 저장하세요.
선택적으로 컴퓨터 간에 암호화된 기록을 동기화하세요.
더 많은 정보: <https://atuin.sh/docs/commands>.

- 쉘에 atuin 설치:

`eval "$(atuin init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|zsh|fish</span>`)"`

- 쉘 기본 기록 파일에서 기록 가져오기:

`atuin import auto`

- 특정 명령에 대한 쉘 기록 검색:

`atuin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 기본 동기화 서버에 계정 등록:

`atuin register -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 기본 동기화 서버에 로그인:

`atuin login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 동기화 서버와의 동기화 기록:

`atuin sync`
