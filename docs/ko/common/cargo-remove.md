---
layout: page
title: common/cargo-remove (한국어)
description: "Rust 프로젝트의 `Cargo.toml` 매니페스트에서 종속성을 제거."
content_hash: 89843d390d58dc68f72a39920a51c7c5de918662
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-remove.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo remove

Rust 프로젝트의 `Cargo.toml` 매니페스트에서 종속성을 제거.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- 현재 프로젝트에서 종속성을 제거:

`cargo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종속성</span>

- 개발 또는 빌드 종속성을 제거:

`cargo remove --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종속성</span>

- 특정 대상 플랫폼의 종속성을 제거:

`cargo remove --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종속성</span>
