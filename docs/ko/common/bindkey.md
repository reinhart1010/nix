---
layout: page
title: common/bindkey (한국어)
description: "Z-Shell에 키 바인딩을 추가."
content_hash: e6b95bae949b37396374da5bc17454c3df714dc9
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/bindkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bindkey

Z-Shell에 키 바인딩을 추가.
더 많은 정보: <https://zsh.sourceforge.io/Guide/zshguide04.html>.

- 특정 명령에 단축키를 바인딩:

`bindkey "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^k</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kill-line</span>

- 핫키를 특정 키 시퀀스([s]equence)에 바인딩:

`bindkey -s '^o' 'cd ..\n'`

- 키맵의 목록([l]ist)을 출력:

`bindkey -l`

- 키맵(key[M]ap)에서 단축키 보기:

`bindkey -M main`
