---
layout: page
title: linux/chfn (한국어)
description: "사용자의 `finger` 정보를 업데이트."
content_hash: 806cc325e25ea287a59dcd47e0c54f9a9571508f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/chfn.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/chfn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chfn

사용자의 `finger` 정보를 업데이트.
더 많은 정보: <https://manned.org/chfn>.

- `finger` 출력에서 사용자의 "이름" 필드를 업데이트:

`chfn -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_표시_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- `finger` 출력에서 사용자의 "사무실 방 번호" 필드를 업데이트:

`chfn -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_사무실_방_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- `finger` 출력에서 사용자의 "사무실 전화번호" 필드를 업데이트:

`chfn -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_사무실_전화번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- `finger` 출력에서 사용자의 "집 전화번호" 필드를 업데이트:

`chfn -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_집_전화번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
