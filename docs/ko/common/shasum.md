---
layout: page
title: common/shasum (한국어)
description: "SHA 암호화 체크섬 계산."
content_hash: 86d454b8936c4793302da243d451b8d3707e8bc4
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/shasum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/shasum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/shasum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shasum

SHA 암호화 체크섬 계산.
더 많은 정보: <https://manned.org/shasum>.

- 하나 이상의 파일에 대해 SHA1 체크섬 계산:

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 하나 이상의 파일에 대해 SHA256 체크섬 계산:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 하나 이상의 파일에 대해 SHA512 체크섬 계산:

`shasum --algorithm 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- `stdin`에서 SHA1 체크섬 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | shasum`

- SHA256 체크섬 목록을 파일에 계산 및 저장:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha256</span>

- SHA1 체크섬 및 파일 이름 목록이 포함된 파일을 읽어 모든 파일이 일치하는지 검증:

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 누락된 파일 또는 검증 실패 시에만 메시지 표시:

`shasum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 누락된 파일은 무시하고 검증 실패 시에만 메시지 표시:

`shasum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
