---
layout: page
title: common/cargo-owner (한국어)
description: "레지스트리에서 크레이트의 소유자를 관리."
content_hash: f33e015b6aa00d427df10b0f9fd47c563c4cc17f
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-owner.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-owner.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo owner

레지스트리에서 크레이트의 소유자를 관리.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- 특정 사용자나 팀을 소유자로 초대:

`cargo owner --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|github:조직_이름:팀_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트</span>

- 지정된 사용자 또는 팀을 소유자로 제거:

`cargo owner --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명|github:조직_이름:팀_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트</span>

- 크레이트 소유자 목록:

`cargo owner --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트</span>

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo owner --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
