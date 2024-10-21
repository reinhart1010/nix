---
layout: page
title: common/gcrane-gc (한국어)
description: "태그가 지정되지 않은 이미지를 나열."
content_hash: ebcd29c6d41571ad4b2ea03803ebc3551b72b192
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gcrane-gc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane gc

태그가 지정되지 않은 이미지를 나열.
가비지 수집이 가능한 이미지를 계산.
`gcrane delete`로 구성하여 실제로 가비지 수집할 수 있음.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 태그가 지정되지 않은 이미지 목록:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>

- 레포지토리를 통해 반복할지 여부:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- 도움말 표시:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
