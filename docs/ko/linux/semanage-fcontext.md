---
layout: page
title: linux/semanage-fcontext (한국어)
description: "파일/폴더에 대한 지속적인 SELinux 보안 컨텍스트 규칙 관리."
content_hash: ad2ae667eb5b2c85daaef9ab6e2a680fb881e2ac
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/semanage-fcontext.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/semanage-fcontext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# semanage fcontext

파일/폴더에 대한 지속적인 SELinux 보안 컨텍스트 규칙 관리.
같이 보기: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
더 많은 정보: <https://manned.org/semanage-fcontext>.

- 모든 파일 레이블링 규칙 나열:

`sudo semanage fcontext --list`

- 사용자 정의 파일 레이블링 규칙을 헤더 없이 나열:

`sudo semanage fcontext --list --locallist --noheading`

- PCRE 정규표현식과 일치하는 경로에 레이블을 지정하는 사용자 정의 규칙 추가:

`sudo semanage fcontext --add --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samba_share_t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'/mnt/share(/.*)?'</span>

- PCRE 정규표현식을 사용하여 사용자 정의 규칙 삭제:

`sudo semanage fcontext --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'/mnt/share(/.*)?'</span>

- 새로운 규칙을 적용하여 폴더를 재귀적으로 다시 레이블링:

`restorecon -R -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
