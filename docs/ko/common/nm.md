---
layout: page
title: common/nm (한국어)
description: "오브젝트 파일에서 심볼 이름을 나열합니다."
content_hash: 988ea306c396e8c0fa887a9185ebc47acf52ea82
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nm

오브젝트 파일에서 심볼 이름을 나열합니다.
더 많은 정보: <https://manned.org/nm>.

- 파일에서 전역(외부) 함수 나열 (T로 시작):

`nm -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>

- 파일에서 정의되지 않은 심볼만 나열:

`nm -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>

- 디버깅 심볼까지 모든 심볼 나열:

`nm -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>

- C++ 심볼을 디망글 (읽기 쉽게 변환):

`nm --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.o</span>
