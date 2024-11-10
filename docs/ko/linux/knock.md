---
layout: page
title: linux/knock (한국어)
description: "방화벽의 특정 포트를 열기 위한 포트 노킹 클라이언트."
content_hash: 94dcde8024f1a0ceca150a69aebd228b58156896
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/knock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# knock

방화벽의 특정 포트를 열기 위한 포트 노킹 클라이언트.
더 많은 정보: <https://manned.org/knock>.

- 다른 프로토콜을 사용하여 포트 노킹:

`knock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜</span>

- UDP를 사용하여 포트 노킹:

`knock -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>

- IPv4/IPv6 강제 사용:

`knock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4|-6</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>

- 연결 오류 및 세부 정보 표시:

`knock -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트번호</span>
