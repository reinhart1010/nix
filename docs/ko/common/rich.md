---
layout: page
title: common/rich (한국어)
description: "터미널에서 화려한 출력을 위한 도구 모음."
content_hash: 2ebbb441a7a7c94296d6634307309a5b9c51b01f
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/rich.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rich

터미널에서 화려한 출력을 위한 도구 모음.
더 많은 정보: <https://github.com/Textualize/rich-cli>.

- 파일을 구문 강조와 함께 표시:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 줄 번호 및 들여쓰기 가이드 추가:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>` --line-number --guides`

- 테마 적용:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>` --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monokai</span>

- 파일을 인터랙티브 페이지로 표시:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>` --pager`

- URL에서 내용 표시:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md</span>` --markdown --pager`

- 파일을 HTML로 내보내기:

`rich `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md</span>` --export-html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html</span>

- 서식 태그, 사용자 정의 정렬 및 줄 너비를 사용하여 텍스트 표시:

`rich --print "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello [green on black]Stylized[/green on black] [bold]World[/bold]</span>`" --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|center|right</span>` --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
