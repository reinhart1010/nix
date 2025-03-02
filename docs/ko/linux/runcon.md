---
layout: page
title: linux/runcon (한국어)
description: "프로그램을 다른 SELinux 보안 컨텍스트에서 실행."
content_hash: 6b7fb171ba2d6579880a279b2dd2c3e8b4a5bd1f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/runcon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/runcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runcon

프로그램을 다른 SELinux 보안 컨텍스트에서 실행.
같이 보기: `secon`.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- 현재 실행 컨텍스트의 보안 컨텍스트를 출력:

`runcon`

- 명령을 실행할 도메인 지정:

`runcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령을 실행할 컨텍스트 역할 지정:

`runcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>`_r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령을 실행할 전체 컨텍스트 지정:

`runcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`_u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>`_r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
