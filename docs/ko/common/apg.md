---
layout: page
title: common/apg (한국어)
description: "임의로 복잡한 랜덤 암호를 만듭니다."
content_hash: b01557ea4d624dfd046461757d7ad9abfe13da30
last_modified_at: 2023-05-22
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
---
# apg

임의로 복잡한 랜덤 암호를 만듭니다.
더 많은 정보: <https://manned.org/apg>.

- 임의 비밀번호 생성 (기본 비밀번호 길이는 8):

`apg`

- 1개 이상의 기호(S), 1개의 숫자(N), 1개의 대문자(C), 1개의 소문자(L) 로 비밀번호 생성:

`apg -M SNCL`

- 16개 글자의 비밀번호 생성:

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- 최대 길이가 16인 비밀번호 생성:

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- 사전에 나타나지 않는 암호를 생성(사전 파일을 제공해야함):

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리_파일</span>
