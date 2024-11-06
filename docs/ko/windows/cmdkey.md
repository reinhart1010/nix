---
layout: page
title: windows/cmdkey (한국어)
description: "저장된 사용자 이름 및 비밀번호를 생성, 표시, 삭제."
content_hash: fab4bbbddaab92d61b3dc179c153dba6825ef266
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/cmdkey.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmdkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmdkey

저장된 사용자 이름 및 비밀번호를 생성, 표시, 삭제.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>.

- 모든 사용자 자격 증명 나열:

`cmdkey /list`

- 서버에 액세스하는 사용자의 자격 증명 저장:

`cmdkey /add:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_이름</span>` /user:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 특정 대상의 자격 증명 삭제:

`cmdkey /delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_이름</span>
