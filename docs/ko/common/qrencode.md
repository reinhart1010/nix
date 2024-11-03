---
layout: page
title: common/qrencode (한국어)
description: "QR 코드 생성기. PNG와 EPS를 지원합니다."
content_hash: cf176ee59fb755fb86f0098b124f863a12321b56
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/qrencode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qrencode

QR 코드 생성기. PNG와 EPS를 지원합니다.
더 많은 정보: <https://fukuchi.org/works/qrencode>.

- 문자열을 QR 코드로 변환하여 출력 파일로 저장:

`qrencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 입력 파일을 QR 코드로 변환하여 출력 파일로 저장:

`qrencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.png</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 문자열을 QR 코드로 변환하여 터미널에 출력:

`qrencode -t ansiutf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 파이프로부터 입력을 받아 QR 코드로 변환하여 터미널에 출력:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` | qrencode -t ansiutf8`
