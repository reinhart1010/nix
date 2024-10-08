---
layout: page
title: common/git-fsck (한국어)
description: "Git 저장소 색인의 노드 유효성과 연결성을 확인."
content_hash: bde9f6c051aca5398a2881948b15c79e23a09b57
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-fsck.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fsck.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git fsck

Git 저장소 색인의 노드 유효성과 연결성을 확인.
수정 작업은 수행하지 않음.
같이 보기: `git gc` (dangling blobs 정리).
더 많은 정보: <https://git-scm.com/docs/git-fsck>.

- 현재 저장소 확인:

`git fsck`

- 발견된 모든 태그 나열:

`git fsck --tags`

- 발견된 모든 루트 노드 나열:

`git fsck --root`
