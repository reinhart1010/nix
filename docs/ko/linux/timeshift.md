---
layout: page
title: linux/timeshift (한국어)
description: "시스템 복원 도구."
content_hash: 1b6ac50dcfa0892db13da62cf99153b96203021b
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/timeshift.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timeshift

시스템 복원 도구.
더 많은 정보: <https://github.com/teejee2008/timeshift>.

- 스냅샷 나열:

`sudo timeshift --list`

- 새 스냅샷 생성 (예약된 경우):

`sudo timeshift --check`

- 새 스냅샷 생성 (예약되지 않은 경우에도):

`sudo timeshift --create`

- 스냅샷 복원 (상호작용을 통해 복원할 스냅샷 선택):

`sudo timeshift --restore`

- 특정 스냅샷 복원:

`sudo timeshift --restore --snapshot '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷</span>`'`

- 특정 스냅샷 삭제:

`sudo timeshift --delete --snapshot '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷</span>`'`
