---
layout: page
title: linux/pidof (한국어)
description: "프로세스 이름을 사용하여 프로세스 ID를 가져옵니다."
content_hash: 1488a69b37069af4ed67e3bf6f79529be224ab9d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pidof.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pidof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pidof

프로세스 이름을 사용하여 프로세스 ID를 가져옵니다.
더 많은 정보: <https://manned.org/pidof>.

- 주어진 이름의 모든 프로세스 ID 나열:

`pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- 주어진 이름의 단일 프로세스 ID 나열:

`pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- 주어진 이름의 스크립트를 포함한 프로세스 ID 나열:

`pidof -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.py</span>

- 주어진 이름의 모든 프로세스를 종료:

`kill $(pidof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`)`
