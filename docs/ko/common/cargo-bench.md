---
layout: page
title: common/cargo-bench (한국어)
description: "벤치마크를 컴파일하고 실행."
content_hash: 4b6eef5130f0bd84e990dc8265cfc4e3c67ca29f
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-bench.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-bench.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo bench

벤치마크를 컴파일하고 실행.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- 패키지의 모든 벤치마크를 실행:

`cargo bench`

- 벤치마크가 실패하더라도 중단하지 않음:

`cargo bench --no-fail-fast`

- 컴파일하지만, 벤치마크를 실행하지 않음:

`cargo bench --no-run`

- 지정된 벤치마크를 벤치마킹:

`cargo bench --bench `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">벤치마크</span>

- 주어진 프로필을 사용한 벤치마크 (기본값: `bench`):

`cargo bench --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필</span>

- 모든 예시 타겟을 벤치마킹:

`cargo bench --examples`

- 모든 바이너리 타겟을 벤치마킹:

`cargo bench --bins`

- 패키지 라이브러리를 벤치마킹:

`cargo bench --lib`
