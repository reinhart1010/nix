---
layout: page
title: common/gcrane-ls (한국어)
description: "저장소의 태그 나열."
content_hash: b25dc2f7286d54ca1e5080930d1db181de325b7e
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gcrane-ls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane ls

저장소의 태그 나열.
태그, 매니페스트 및 하위 저장소를 나열할 수 있는 `crane ls`보다 더 복잡한 형식.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 태그 목록 나열:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>

- 레지스트리의 응답 형식을 JSON으로 지정:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>` --json`

- 레포지토리를 통해 반복할지 여부 결정:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- 도움말 표시:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
