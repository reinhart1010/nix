---
layout: page
title: common/sha384sum (한국어)
description: "SHA384 암호화 체크섬 계산."
content_hash: b088bcfa18d4b7b53a2c6901df9b63705f9c38a5
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/sha384sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sha384sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha384sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sha384sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sha384sum

SHA384 암호화 체크섬 계산.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- 하나 이상의 파일에 대한 SHA384 체크섬 계산:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- SHA384 체크섬 목록을 파일에 계산 및 저장:

`sha384sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha384</span>

- `stdin`에서 SHA384 체크섬 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sha384sum`

- SHA384 체크섬과 파일 이름 목록이 포함된 파일을 읽어 모든 파일이 일치하는지 검증:

`sha384sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha384</span>

- 누락된 파일 또는 검증 실패 시에만 메시지 표시:

`sha384sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha384</span>

- 누락된 파일은 무시하고 검증 실패 시에만 메시지 표시:

`sha384sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sha384</span>
