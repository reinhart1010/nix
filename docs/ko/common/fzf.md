---
layout: page
title: common/fzf (한국어)
description: "명령줄 퍼지 찾기."
content_hash: 33157220a620d3943bfd198ce2f92fb356fa916f
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fzf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fzf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/fzf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fzf

명령줄 퍼지 찾기.
`sk`와 유사.
더 많은 정보: <https://github.com/junegunn/fzf>.

- 지정된 디렉터리의 모든 파일에서 `fzf`를 시작:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` -type f | fzf`

- 프로세스 실행을 위해 `fzf`를 시작:

`ps aux | fzf`

- `Shift + Tab`을 사용해 여러 파일을 선택하고 파일에 작성:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 쿼리로 `fzf`를 시작:

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`"`

- core로 시작하고 go, rb 또는 py로 끝나는 항목에서 `fzf`를 시작:

`fzf --query "^core go$ | rb$ | py$"`

- pvc와 일치하지 않고 travis와 정확히 일치하는 항목에 대해 `fzf`를 시작:

`fzf --query "!pyc 'travis"`
