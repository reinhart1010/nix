---
layout: page
title: common/htpasswd (한국어)
description: "기본 인증을 사용하여 웹 서버 폴더를 보호하기 위해 htpasswd 파일을 생성하고 관리합니다."
content_hash: 4e2fa7bcb88121581e80d8f387065221c06cedc0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/htpasswd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htpasswd

기본 인증을 사용하여 웹 서버 폴더를 보호하기 위해 htpasswd 파일을 생성하고 관리합니다.
더 많은 정보: <https://httpd.apache.org/docs/current/programs/htpasswd.html>.

- htpasswd 파일 생성/덮어쓰기:

`htpasswd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- htpasswd 파일에 사용자 추가 또는 기존 사용자 업데이트:

`htpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 대화형 비밀번호 프롬프트 없이 배치 모드에서 htpasswd 파일에 사용자 추가(스크립트 사용 목적):

`htpasswd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- htpasswd 파일에서 사용자 삭제:

`htpasswd -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 사용자 비밀번호 확인:

`htpasswd -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 사용자 이름(일반 텍스트) 및 비밀번호(md5)가 포함된 문자열 표시:

`htpasswd -nbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
