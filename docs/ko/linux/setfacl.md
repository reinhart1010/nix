---
layout: page
title: linux/setfacl (한국어)
description: "파일 접근 제어 목록(ACL) 설정."
content_hash: b733dd745c1da817bbd26ed99771fee42a3a4fca
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/setfacl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setfacl

파일 접근 제어 목록(ACL) 설정.
더 많은 정보: <https://manned.org/setfacl>.

- [u]사용자에게 읽기 및 쓰기 권한으로 파일의 ACL [m]수정:

`setfacl --modify u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`:rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 모든 사용자에 대한 파일의 기본 ACL [m]수정:

`setfacl --modify --default u::rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 파일의 사용자에 대한 ACL 제거:

`setfacl --remove u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 파일의 모든 ACL 항목 제거:

`setfacl --remove-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
