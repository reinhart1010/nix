---
layout: page
title: common/rage (한국어)
description: "간단하고 안전하며 현대적인 파일 암호화 도구(Rust 라이브러리 포함)로, 작은 명시적 키, 설정 옵션 없음, UNIX 스타일의 구성 가능성을 제공합니다."
content_hash: b6a8f1b9574cfdfbd04b449496adc08029963ba2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rage.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rage.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rage

간단하고 안전하며 현대적인 파일 암호화 도구(Rust 라이브러리 포함)로, 작은 명시적 키, 설정 옵션 없음, UNIX 스타일의 구성 가능성을 제공합니다.
`age`의 Rust 구현.
더 많은 정보: <https://github.com/str4d/rage>.

- `user`를 위한 파일을 암호화하고 `message.age`로 저장:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">당신의 비밀 메시지</span>`" | rage --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/message.age</span>

- `identity_file`로 파일을 복호화하고 `message`로 저장:

`rage --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/identity_file</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>
