---
layout: page
title: common/cargo-clean (한국어)
description: "`target` 디렉터리에서 생성된 아티팩트를 제거."
content_hash: 3daf2e0065a89f1479e6ebdbf85adb712fd86a61
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-clean.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo clean

`target` 디렉터리에서 생성된 아티팩트를 제거.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- 전체 `target` 디렉터리를 제거:

`cargo clean`

- 문서 아티팩트 제거 (`target/doc` 디렉터리):

`cargo clean --doc`

- 릴리스 아티팩트 제거 (`target/release` 디렉터리):

`cargo clean --release`

- 지정된 프로필의 디렉터리에서 아티팩트를 제거 (이 경우, `target/debug`):

`cargo clean --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev</span>
