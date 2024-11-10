---
layout: page
title: common/stl2gts (한국어)
description: "STL 파일을 GTS(GNU 삼각형 표면 라이브러리) 파일 형식으로 변환."
content_hash: bc98c5a7d15e9854eb3972f2292335358f85c454
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stl2gts.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/stl2gts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stl2gts

STL 파일을 GTS(GNU 삼각형 표면 라이브러리) 파일 형식으로 변환.
더 많은 정보: <https://manned.org/stl2gts>.

- STL 파일을 GTS 파일로 변환:

`stl2gts < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gts</span>

- STL 파일을 GTS 파일로 변환하고 면의 법선을 뒤집기:

`stl2gts --revert < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gts</span>

- STL 파일을 GTS 파일로 변환하고 정점 병합 안 함:

`stl2gts --nomerge < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gts</span>

- STL 파일을 GTS 파일로 변환하고 표면 통계 표시:

`stl2gts --verbose < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.stl</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gts</span>

- 도움말 표시:

`stl2gts --help`
