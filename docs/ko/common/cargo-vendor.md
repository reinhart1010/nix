---
layout: page
title: common/cargo-vendor (한국어)
description: "프로젝트의 모든 종속성을 지정된 디렉터리에 공급 (기본값: `vendor`)."
content_hash: 00169a482b0cfd4e6cf6140ba1ad38a05b641dae
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-vendor.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-vendor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo vendor

프로젝트의 모든 종속성을 지정된 디렉터리에 공급 (기본값: `vendor`).
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>.

- 공급업체 종속성 및 현재 프로젝트에서 공급업체 소스를 사용하도록 `cargo`를 구성:

`cargo vendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` > .cargo/config.toml`
