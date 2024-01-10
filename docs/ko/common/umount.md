---
layout: page
title: common/umount (한국어)
description: "마운트 지점에서 파일 시스템이 링크를 해제하여 더 이상 접근할 수 없게 만들어 줍니다."
content_hash: 32c6984103c4bcccf09e67dbc71e799822e8b697
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/umount.html
    icon: bi bi-globe
tldri18n_status: 2
---
# umount

마운트 지점에서 파일 시스템이 링크를 해제하여 더 이상 접근할 수 없게 만들어 줍니다.
파일 시스템이 사용중이면 마운트 해제할 수 없습니다.
더 많은 정보: <https://man.openbsd.org/umount>.

- 마운트된 소스의 경로를 전달하여, 파일 시스템을 마운트 해제:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>

- 파일 시스템이 마운트된 대상에 대한 경로를 전달하여 파일 시스템 마운트 해제:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트된_폴더</span>

- 마운트된 모든 파일 시스템을 마운트 해제(`proc` 파일 시스템 제외):

`umount -a`
