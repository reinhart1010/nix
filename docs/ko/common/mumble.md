---
layout: page
title: common/mumble (한국어)
description: "저지연, 고품질 음성 채팅 소프트웨어."
content_hash: 21a10254828c98324a8746f93f5aac4a811a2a4a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mumble.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mumble.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mumble

저지연, 고품질 음성 채팅 소프트웨어.
더 많은 정보: <https://www.mumble.info>.

- Mumble 열기:

`mumble`

- Mumble을 열고 즉시 서버에 연결:

`mumble mumble://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.com</span>

- Mumble을 열고 즉시 비밀번호로 보호된 서버에 연결:

`mumble mumble://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예제.com</span>

- 실행 중인 Mumble 인스턴스에서 마이크 음소거/음소거 해제:

`mumble rpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mute|unmute</span>

- Mumble의 마이크 및 오디오 출력 음소거/음소거 해제:

`mumble rpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deaf|undeaf</span>
