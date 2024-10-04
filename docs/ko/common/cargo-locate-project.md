---
layout: page
title: common/cargo-locate-project (한국어)
description: "프로젝트의 `Cargo.toml` 매니페스트에 대한 전체 경로를 인쇄."
content_hash: ea333a72aef0945a18ca13f955812d6a1808b469
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-locate-project.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-locate-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo locate-project

프로젝트의 `Cargo.toml` 매니페스트에 대한 전체 경로를 인쇄.
프로젝트가 작업공간의 일부인 경우, 작업공간의 매니페스트가 아닌 프로젝트의 매니페스트가 표시됨.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- `Cargo.toml` 매니페스트에 대한 전체 경로가 포함된 JSON 객체를 표시:

`cargo locate-project`

- 지정된 형식으로 프로젝트 경로를 표시:

`cargo locate-project --message-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain|json</span>

- 현재 작업공간 멤버가 아닌 작업공간 루트에 있는 `Cargo.toml` 매니페스트를 표시:

`cargo locate-project --workspace`

- 특정 디렉터리의 `Cargo.toml` 매니페스트를 표시:

`cargo locate-project --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Cargo.toml</span>
