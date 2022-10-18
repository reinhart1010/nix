---
layout: page
title: common/tmux (한국어)
description: "터미널 멀티플렉서. tmux는 단일 단말기 창 또는 원격 터미널 세션 안에서 여러 세션을 사용할 수 있도록 도와줍니다."
content_hash: 26e349070e06a76a6350d96af24becab8bfb23ec
related_topics:
  - title: English version
    url: /en/common/tmux.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tmux.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tmux.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/tmux.html
    icon: bi bi-globe
---
# tmux

터미널 멀티플렉서. tmux는 단일 단말기 창 또는 원격 터미널 세션 안에서 여러 세션을 사용할 수 있도록 도와줍니다.
`zellij` 와 `screen`도 참조하세요.
더 많은 정보: <https://github.com/tmux/tmux>.

- 새 세션 시작:

`tmux`

- 이름있는 새 세션 시작:

`tmux new -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 세션 리스트 출력:

`tmux ls`

- 가장 최근에 사용했던 세션에 접근:

`tmux attach`

- 현재 세션에서 나가기 (tmux 세션 안에서 사용):

`Ctrl-B d`

- 새 창 만들기 (tmux 세션 안에서 사용):

`Ctrl-B c`

- 세션 혹은 창 변경 (tmux 세션 안에서 사용):

`Ctrl-B w`

- 세션 이름으로 종료:

`tmux kill-session -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
