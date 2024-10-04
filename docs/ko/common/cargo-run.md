---
layout: page
title: common/cargo-run (한국어)
description: "현재 Cargo 패키지를 실행."
content_hash: 81cfc270e16092ce8c0e1b48f16c9b0dca97faa3
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-run.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo run

현재 Cargo 패키지를 실행.
참고: 실행된 바이너리의 작업 디렉터리는 현재 작업 디렉터리로 설정됨.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- 기본 바이너리 타겟을 실행:

`cargo run`

- 지정된 바이너리를 실행:

`cargo run --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 지정된 예제를 실행:

`cargo run --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 공백 또는 쉼표로 구분된 기능 목록을 활성화:

`cargo run --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능1 기능2 ...</span>

- 기본 기능을 비활성화:

`cargo run --no-default-features`

- 사용 가능한 모든 기능을 활성화:

`cargo run --all-features`

- 주어진 프로필로 실행:

`cargo run --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
