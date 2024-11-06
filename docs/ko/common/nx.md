---
layout: page
title: common/nx (한국어)
description: "`nx` 작업 공간 관리 도구."
content_hash: df3d38d2bc1cdcd8cf7293c4d50125ee056949f7
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nx

`nx` 작업 공간 관리 도구.
더 많은 정보: <https://nx.dev/l/r/getting-started/nx-cli>.

- 특정 프로젝트 빌드:

`nx build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트</span>

- 특정 프로젝트 테스트:

`nx test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트</span>

- 특정 프로젝트에서 대상 실행:

`nx run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 여러 프로젝트에서 대상 실행:

`nx run-many --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` --projects `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트2</span>

- 작업 공간의 모든 프로젝트에서 대상 실행:

`nx run-many --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>` --all`

- 변경된 프로젝트에서만 대상 실행:

`nx affected --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>
