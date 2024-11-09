---
layout: page
title: linux/exec (한국어)
description: "자식 프로세스를 생성하지 않고 명령을 실행합니다."
content_hash: 9991097406cf2088e842fd84c40afa642a93f2de
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/exec.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exec

자식 프로세스를 생성하지 않고 명령을 실행합니다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- 특정 명령 실행:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 -옵션 -플래그</span>

- (거의) 빈 환경에서 명령 실행:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 -옵션 -플래그</span>

- 로그인 셸로 명령 실행:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 -옵션 -플래그</span>

- 다른 이름으로 명령 실행:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 -옵션 -플래그</span>
