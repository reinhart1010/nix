---
layout: page
title: common/errno (한국어)
description: "오류 번호 이름과 설명을 검색."
content_hash: 937b1b9f4c4a2ac18bd745fbdad5c150e6436d63
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/errno.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/errno.html
    icon: bi bi-globe
tldri18n_status: 2
---
# errno

오류 번호 이름과 설명을 검색.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 이름이나 코드로 오류 번호 설명 조회:

`errno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|code</span>

- 모든 오류 번호 이름, 코드 및 설명을 나열:

`errno --list`

- 설명에 주어진 텍스트가 모두 포함된 코드를 검색:

`errno --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>

- 설명에 주어진 텍스트 (모든 로케일)가 모두 포함된 코드를 검색:

`errno --search-all-locales `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>
