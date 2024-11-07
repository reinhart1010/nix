---
layout: page
title: common/lpass (한국어)
description: "LastPass 비밀번호 관리자의 명령줄 인터페이스."
content_hash: 3430744bcdd13c1b2f4c5d5fae25e2b29aa70dee
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpass

LastPass 비밀번호 관리자의 명령줄 인터페이스.
더 많은 정보: <https://github.com/lastpass/lastpass-cli>.

- 마스터 비밀번호를 입력하여 LastPass 계정에 로그인:

`lpass login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>

- 로그인 상태 표시:

`lpass status`

- 카테고리별로 그룹화된 모든 사이트 나열:

`lpass ls`

- `myinbox` 식별자로 gmail.com의 새 비밀번호 생성 및 LastPass에 추가:

`lpass generate --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>` --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gmail.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myinbox</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호_길이</span>

- 지정된 항목의 비밀번호 표시:

`lpass show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">myinbox</span>` --password`
