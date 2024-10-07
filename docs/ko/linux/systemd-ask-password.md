---
layout: page
title: linux/systemd-ask-password (한국어)
description: "시스템 비밀번호를 사용자에게 요청."
content_hash: 429ad14c1663a9858a336a453fc373377bb53f8e
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-ask-password.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-ask-password.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-ask-password

시스템 비밀번호를 사용자에게 요청.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-ask-password.html>.

- 특정 메시지와 함께 시스템 비밀번호 요청:

`systemd-ask-password "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 비밀번호 요청에 식별자 지정:

`systemd-ask-password --id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">식별자</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 커널 키링 키 이름을 비밀번호 캐시로 사용:

`systemd-ask-password --keyname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 비밀번호 요청에 사용자 정의 시간 초과 설정:

`systemd-ask-password --timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 에이전트 시스템을 강제로 사용하고 현재 TTY에서 묻지 않음:

`systemd-ask-password --no-tty "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 비밀번호를 표시하지 않고 커널 키링에 저장:

`systemd-ask-password --no-output --keyname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`
