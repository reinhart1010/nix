---
layout: page
title: common/git-standup (한국어)
description: "지정된 사용자의 커밋을 확인."
content_hash: 10b6f4d73c67ddef6015a8fb14521ebbce20a39f
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-standup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git standup

지정된 사용자의 커밋을 확인.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-standup>.

- 지정된 작성자의 최근 10일간의 커밋 보기:

`git standup -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|이메일</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 지정된 작성자의 최근 10일간의 커밋 및 GPG 서명 여부 확인:

`git standup -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|이메일</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -g`

- 최근 10일간 모든 기여자의 모든 커밋 보기:

`git standup -a all -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 도움말 표시:

`git standup -h`
