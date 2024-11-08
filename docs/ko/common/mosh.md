---
layout: page
title: common/mosh (한국어)
description: "Mobile Shell (`mosh`)는 SSH를 대체하는 강력하고 반응성이 뛰어난 도구입니다."
content_hash: e444f89d1119214dd17d6b411264560c5434bb4b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mosh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mosh

Mobile Shell (`mosh`)는 SSH를 대체하는 강력하고 반응성이 뛰어난 도구입니다.
`mosh`는 네트워크를 이동하면서도 원격 서버와의 연결을 지속합니다.
더 많은 정보: <https://mosh.org>.

- 원격 서버에 연결:

`mosh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 특정 신원(개인 키)으로 원격 서버에 연결:

`mosh --ssh="ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 특정 포트를 사용하여 원격 서버에 연결:

`mosh --ssh="ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 원격 서버에서 명령 실행:

`mosh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 -옵션들</span>

- Mosh UDP 포트 선택 (`원격_호스트`가 NAT 뒤에 있을 때 유용):

`mosh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">124</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- `mosh-server` 바이너리가 표준 경로 외부에 있을 때 사용법:

`mosh --server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리/</span>`mosh-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>
