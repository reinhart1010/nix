---
layout: page
title: linux/setfattr (한국어)
description: "확장 파일 속성 설정."
content_hash: 41a50f439c8188604b9dc298bc1241a29ad2f4ba
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setfattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setfattr

확장 파일 속성 설정.
더 많은 정보: <https://manned.org/setfattr>.

- 파일의 속성 이름 설정:

`setfattr -n user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 사용자 정의 확장 속성 값 설정:

`setfattr -n user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>` -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 특정 속성 제거:

`setfattr -x user.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
