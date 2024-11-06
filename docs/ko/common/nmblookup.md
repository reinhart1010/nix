---
layout: page
title: common/nmblookup (한국어)
description: "SMB 공유를 검색."
content_hash: cf880e590d0519bcd5fba99e27ac7b57643b88b1
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nmblookup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmblookup

SMB 공유를 검색.
더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/nmblookup.1.html>.

- 로컬 네트워크에서 SMB 공유가 있는 호스트 찾기:

`nmblookup -S '*'`

- SAMBA에 의해 실행되는 SMB 공유가 있는 로컬 네트워크의 호스트 찾기:

`nmblookup --status __SAMBA__`
