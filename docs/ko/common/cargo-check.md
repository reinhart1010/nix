---
layout: page
title: common/cargo-check (한국어)
description: "로컬 패키지와 모든 종속 항목에 오류가 있는지 확인."
content_hash: 40d257b0fbd439c8f51365c01650f9af3e48c20a
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-check.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo check

로컬 패키지와 모든 종속 항목에 오류가 있는지 확인.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- 현재 패키지 검사:

`cargo check`

- 모든 테스트 검사:

`cargo check --tests`

- `tests/integration_test1.rs`에서 통합 테스트를 확인:

`cargo check --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">통합_테스트1</span>

- `feature1` 및 `feature2` 기능이 포함된 현재 패키지를 확인:

`cargo check --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능1,기능2</span>

- 기본 기능이 비활성화된 현재 패키지 확인:

`cargo check --no-default-features`
