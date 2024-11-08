---
layout: page
title: common/loc (한국어)
description: "코드의 줄 수를 계산합니다. Rust로 작성되었습니다."
content_hash: 4dbe8ad447bf5c3da400b02ece78469b17e004a6
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/loc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# loc

코드의 줄 수를 계산합니다. Rust로 작성되었습니다.
더 많은 정보: <https://github.com/cgag/loc>.

- 현재 디렉토리의 코드 줄 수 출력:

`loc`

- 대상 디렉토리의 코드 줄 수 출력:

`loc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 개별 파일에 대한 통계와 함께 코드 줄 수 출력:

`loc --files`

- .gitignore (등) 파일을 제외하고 코드 줄 수 출력 (예: `-u` 플래그를 두 번 사용하면 숨겨진 파일과 디렉토리도 추가로 계산):

`loc -u`
