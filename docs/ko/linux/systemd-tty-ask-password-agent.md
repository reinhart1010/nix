---
layout: page
title: linux/systemd-tty-ask-password-agent (한국어)
description: "보류 중인 systemd 비밀번호 요청 목록을 표시하거나 처리합니다."
content_hash: c012cd1342c7e42be90e5eb0d2bec405cce939a6
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-tty-ask-password-agent.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-tty-ask-password-agent.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-tty-ask-password-agent

보류 중인 systemd 비밀번호 요청 목록을 표시하거나 처리합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-tty-ask-password-agent.html>.

- 현재 보류 중인 모든 시스템 비밀번호 요청 목록 표시:

`systemd-tty-ask-password-agent --list`

- 비밀번호 요청을 지속적으로 처리:

`systemd-tty-ask-password-agent --watch`

- 호출하는 TTY에서 사용자에게 질문하여 현재 보류 중인 시스템 비밀번호 요청 처리:

`systemd-tty-ask-password-agent --query`

- 호출하는 TTY에서 사용자에게 질문하는 대신 wall로 비밀번호 요청 전달:

`systemd-tty-ask-password-agent --wall`
