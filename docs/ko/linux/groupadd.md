---
layout: page
title: linux/groupadd (한국어)
description: "시스템에 사용자 그룹 추가."
content_hash: c34c1568b10667819753c5bd5bab11d3aa7ea4dd
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/groupadd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/groupadd.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/groupadd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groupadd

시스템에 사용자 그룹 추가.
같이 보기: `groups`, `groupdel`, `groupmod`.
더 많은 정보: <https://manned.org/groupadd>.

- 새 그룹 생성:

`sudo groupadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 새 시스템 그룹 생성:

`sudo groupadd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 특정 그룹 ID로 새 그룹 생성:

`sudo groupadd --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>
