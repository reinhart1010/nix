---
layout: page
title: linux/fsck (한국어)
description: "파일 시스템의 무결성을 검사하거나 복구합니다. 명령어 실행 시 파일 시스템은 마운트 해제되어 있어야 합니다."
content_hash: 4fae099bf6cee35193b2efa6c25f3229b34c0ae4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fsck.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/fsck.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsck

파일 시스템의 무결성을 검사하거나 복구합니다. 명령어 실행 시 파일 시스템은 마운트 해제되어 있어야 합니다.
더 많은 정보: <https://manned.org/fsck>.

- 파일 시스템 `/dev/sdXN`의 손상된 블록을 보고:

`sudo fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템 `/dev/sdXN`의 손상된 블록을 보고, 각 블록을 복구할지 사용자에게 상호작용으로 선택하게 함:

`sudo fsck -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템 `/dev/sdXN`의 손상된 블록을 보고, 자동으로 복구:

`sudo fsck -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
