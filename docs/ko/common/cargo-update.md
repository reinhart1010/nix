---
layout: page
title: common/cargo-update (한국어)
description: "`Cargo.lock`에 기록된 종속성을 업데이트."
content_hash: f4cb34392d405b7ee8b4ffa43fd14007fe8d25f5
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-update.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo update

`Cargo.lock`에 기록된 종속성을 업데이트.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-update.html>.

- `Cargo.lock`의 종속성을 가능한 최신버전으로 업데이트함:

`cargo update`

- 업데이트될 내용을 표시하지만, 실제로 잠금 파일을 작성하지는 않음:

`cargo update --dry-run`

- 지정된 종속성만 업데이트함:

`cargo update --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성1</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성2</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성3</span>

- 특정 버전에 대한 특정 종속성을 설정:

`cargo update --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>` --precise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>
