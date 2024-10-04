---
layout: page
title: common/cargo-login (한국어)
description: "레지스트리에서 로컬로 API 토큰을 저장."
content_hash: 556cd2171d78b43dc1de3f5078c842f2281a2ad1
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-login.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo login

레지스트리에서 로컬로 API 토큰을 저장.
토큰은 패키지 레지스트리를 인증하는 데 사용됨. `cargo logout`을 사용하여 제거할 수 있음 .
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-login.html>.

- 로컬 자격 증명 저장소 (`$CARGO_HOME/credentials.toml`에 위치)에 API 토큰을 추가:

`cargo login`

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo login --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
