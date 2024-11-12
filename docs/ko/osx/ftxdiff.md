---
layout: page
title: osx/ftxdiff (한국어)
description: "두 폰트 간의 차이점을 비교합니다."
content_hash: a32207dfaa4b2321299e5fd043c2b8f867862e9f
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/ftxdiff.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ftxdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftxdiff

두 폰트 간의 차이점을 비교합니다.
더 많은 정보: <https://developer.apple.com/fonts>.

- 특정 텍스트 [f]파일에 차이점 출력:

`ftxdiff --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폰트_차이_파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폰트_파일1.ttc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폰트_파일2.ttc</span>

- 출력에 글리프 이름 포함:

`ftxdiff --include-glyph-names`

- 출력에 유니코드 이름 포함:

`ftxdiff --include-unicode-names`
