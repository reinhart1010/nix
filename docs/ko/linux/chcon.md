---
layout: page
title: linux/chcon (한국어)
description: "파일 또는 파일/디렉토리의 SELinux 보안 컨텍스트를 변경합니다."
content_hash: 169fa14c7ea9d9711b8dcd54e9133dc5c3f521c2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/chcon.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/chcon.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/chcon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/chcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chcon

파일 또는 파일/디렉토리의 SELinux 보안 컨텍스트를 변경합니다.
같이 보기: `secon`, `restorecon`, `semanage-fcontext`.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- 파일의 보안 컨텍스트 보기:

`ls -lZ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 참조된 파일을 사용하여, 대상 파일의 보안 내용 변경:

`chcon --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">참조_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_파일</span>

- 파일의 전체 SELinux 보안 컨텍스트 변경:

`chcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">범위/레벨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- SELinux 보안 컨텍스트의 사용자 부분만 변경:

`chcon -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- SELinux 보안 컨텍스트의 역할 부분만 변경:

`chcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- SELinux 보안 컨텍스트의 유형 부분만 변경:

`chcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- SELinux 보안 컨텍스트의 범위/레벨 부분만 변경:

`chcon -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">범위/레벨</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>
