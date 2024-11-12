---
layout: page
title: linux/groupmod (한국어)
description: "시스템에서 기존 사용자 그룹을 수정합니다."
content_hash: 57fd56640b47b2351786e0a6bf40342d9052ec4b
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/groupmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/groupmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groupmod

시스템에서 기존 사용자 그룹을 수정합니다.
같이 보기: `groups`, `groupadd`, `groupdel`.
더 많은 정보: <https://manned.org/groupmod>.

- 그룹 이름 변경:

`sudo groupmod --new-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 그룹 ID 변경:

`sudo groupmod --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>
