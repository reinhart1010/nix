---
layout: page
title: common/cargo-verify-project (한국어)
description: "`Cargo.toml` 매니페스트의 정확성을 확인하고 결과를 JSON 객체로 출력."
content_hash: 52888dc584b064bccbaddba3474ac9ba1f7d4afa
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-verify-project.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-verify-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo verify-project

`Cargo.toml` 매니페스트의 정확성을 확인하고 결과를 JSON 객체로 출력.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-verify-project.html>.

- 현재 프로젝트 매니페스트의 정확성을 확인:

`cargo verify-project`

- 지정된 매니페스트 파일의 정확성을 확인:

`cargo verify-project --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Cargo.toml</span>
