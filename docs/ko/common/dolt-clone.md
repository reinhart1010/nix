---
layout: page
title: common/dolt-clone (한국어)
description: "저장소를 새로운 디렉터리에 복제."
content_hash: f6f30788946ae031cba1a9e8165ce4def08168b3
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/dolt-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dolt clone

저장소를 새로운 디렉터리에 복제.
더 많은 정보: <https://docs.dolthub.com/interfaces/cli#dolt-clone>.

- 기존 저장소를 특정 디렉터리에 복제 (기본값은 저장소 이름):

`dolt clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 기존 저장소를 복제하고 특정 원격값을 추가 (기본값은 origin):

`dolt clone --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- 특정 브랜치만 가져오는 기존 저장소를 복제 (기본값은 모든 브랜치):

`dolt clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- AWS 리전을 사용하여, 리포지토리를 복제 (uses the profile's default region if none is provided):

`dolt clone --aws-region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리전_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- AWS 자격 증명 파일을 사용하여 리포지토리를 복제:

`dolt clone --aws-creds-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- AWS 자격 증명 프로필을 사용하여 리포지토리를 복제 (아무것도 제공되지 않은 경우, 기본 프로필을 사용):

`dolt clone --aws-creds-profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- AWS 자격 증명 유형을 사용하여 리포지토리를 복젴:

`dolt clone --aws-creds-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_타입</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>
