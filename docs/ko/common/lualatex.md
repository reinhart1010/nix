---
layout: page
title: common/lualatex (한국어)
description: "Lua를 사용하여 컴파일하는 TeX의 확장 버전."
content_hash: 9064db8de9e55bd163d17215df1baf768847009e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lualatex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lualatex

Lua를 사용하여 컴파일하는 TeX의 확장 버전.
더 많은 정보: <https://manned.org/lualatex.1>.

- Lua 인터프리터로 작동하도록 `texlua` 시작:

`lualatex`

- Tex 파일을 PDF로 컴파일:

`lualatex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>

- 오류로 중단 없이 Tex 파일 컴파일:

`lualatex -interaction nonstopmode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>

- 특정 출력 파일 이름으로 Tex 파일 컴파일:

`lualatex -jobname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>
