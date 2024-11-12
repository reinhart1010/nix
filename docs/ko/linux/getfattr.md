---
layout: page
title: linux/getfattr (한국어)
description: "파일 이름 및 확장 속성을 표시합니다."
content_hash: 35934012667ce79ce1a5d7094da1d4d336376a0b
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/getfattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# getfattr

파일 이름 및 확장 속성을 표시합니다.
더 많은 정보: <https://manned.org/getfattr>.

- 파일의 모든 확장 속성을 가져와서 자세히 표시:

`getfattr -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 특정 속성 가져오기:

`getfattr -n user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
