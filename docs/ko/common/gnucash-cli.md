---
layout: page
title: common/gnucash-cli (한국어)
description: "GnuCash의 명령줄 버전."
content_hash: 98fb45b8022e59b12c5587cd11899b4e89dd6af0
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gnucash-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnucash-cli

GnuCash의 명령줄 버전.
더 많은 정보: <https://gnucash.org>.

- 파일에 지정된 통화 및 주식에 대한 견적을 받아 출력:

`gnucash-cli --quotes get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gnucash</span>

- `--name`으로 지정된 특정 유형의 재무 보고서를 생성:

`gnucash-cli --report run --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Balance Sheet</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gnucash</span>
