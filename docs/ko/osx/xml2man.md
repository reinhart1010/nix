---
layout: page
title: osx/xml2man (한국어)
description: "MPGL을 mdoc으로 컴파일합니다."
content_hash: 7623d5e2c6bbcba3d90d48a7a55b8a7ebaa37cfc
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/xml2man.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xml2man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xml2man

MPGL을 mdoc으로 컴파일합니다.
더 많은 정보: <https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/HeaderDoc/mpgl/mpgl.html>.

- MPGL 파일을 보기 가능한 man 페이지로 컴파일:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/명령_파일.mxml</span>

- MPGL 파일을 특정 출력 파일로 컴파일:

`xml2man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스_파일.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/서비스_파일.7</span>

- MPGL 파일을 특정 출력 파일로 컴파일하고, 파일이 이미 존재하면 덮어쓰기:

`xml2man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/함수_파일.mxml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/함수_파일.3</span>
