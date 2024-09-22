---
layout: page
title: common/b3sum (한국어)
description: "BLAKE3 암호화 체크섬을 계산."
content_hash: 61feef9efaa07a2f835c0bec74eda30ed3a7ecef
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/b3sum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/b3sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# b3sum

BLAKE3 암호화 체크섬을 계산.
더 많은 정보: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- 하나 이상의 파일에 대한 BLAKE3 체크섬을 계산:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- BLAKE3 체크섬 목록을 게산하고 파일에 저장:

`b3sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b3</span>

- `stdin`에서 BLAKE3 체크섬을 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | b3sum`

- BLAKE3 합계 및 파일 이름이 포함된 파일을 읽고, 모든 파일에 일치하는 체크섬이 있는지 확인:

`b3sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b3</span>

- 누락된 파일이 있거나 확인에 실패한 경우에만 메시지를 표시:

`b3sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b3</span>
