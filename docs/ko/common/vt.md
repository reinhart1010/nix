---
layout: page
title: common/vt (한국어)
description: "VirusTotal의 명령줄 인터페이스."
content_hash: df7e3ec593de3cd54ad6f69d55e9d4f299154721
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/vt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vt

VirusTotal의 명령줄 인터페이스.
이 명령을 사용하려면 VirusTotal 계정의 API 키가 필요합니다.
더 많은 정보: <https://github.com/VirusTotal/vt-cli>.

- 특정 파일을 바이러스 검사:

`vt scan file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- URL을 바이러스 검사:

`vt scan url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 특정 분석에 대한 정보 표시:

`vt analysis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_ID|분석_ID</span>

- 암호화된 Zip 형식으로 파일 다운로드 (프리미엄 계정 필요):

`vt download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_ID</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --zip --zip-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- `vt`를 초기화하거나 재초기화하여 API 키를 대화식으로 입력:

`vt init`

- 도메인에 대한 정보 표시:

`vt domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 특정 URL에 대한 정보 표시:

`vt url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 특정 IP 주소에 대한 정보 표시:

`vt domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>
