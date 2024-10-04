---
layout: page
title: common/cargo-tree (한국어)
description: "Display a tree visualization of a dependency graph."
content_hash: 2da07adaea1de4b6d8a170630f769829c136d071
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo tree

Display a tree visualization of a dependency graph.
참고: 트리에서, `(*)`로 표시된 패키지의 종속성은 이미 그래프의 다른 곳에 표시되었으므로, 반복되지 않음.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-tree.html>.

- 현재 프로젝트의 종속성 트리를 표시:

`cargo tree`

- 지정된 깊이까지의 종속성만 표시 (예: `n`이 1인 경우, 직접적인 종속성만 표시):

`cargo tree --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- 지정된 패키지(및 해당 종속성)를 트리에 표시하지 않음:

`cargo tree --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_스펙</span>

- 반복되는 종속 항목을 모두 표시:

`cargo tree --no-dedupe`

- 일반/빌드/개발 종속성만 표시:

`cargo tree --edges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal|build|dev</span>
