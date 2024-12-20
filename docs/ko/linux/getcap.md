---
layout: page
title: linux/getcap (한국어)
description: "지정한 각 파일의 이름과 권한을 표시하는 명령어."
content_hash: 22c95a4c58a8ca296608d8dda6d026ffb257c0a4
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/getcap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# getcap

지정한 각 파일의 이름과 권한을 표시하는 명령어.
더 많은 정보: <https://manned.org/getcap>.

- 지정한 파일들의 권한 확인:

`getcap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 지정한 폴더 내 모든 파일의 권한을 재귀적으로 확인:

`getcap -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 권한이 설정되지 않은 경우에도 모든 검색된 항목 표시:

`getcap -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
