---
layout: page
title: common/hledger-import (한국어)
description: "하나 이상의 데이터 파일에서 새 거래를 가져와 주요 저널에 추가."
content_hash: 955df46214e3140cf14b4ed6c890bb9c41b4148a
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/hledger-import.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hledger import

하나 이상의 데이터 파일에서 새 거래를 가져와 주요 저널에 추가.
더 많은 정보: <https://hledger.org/hledger.html#import>.

- `bank.csv.rules`를 사용하여 `bank.csv`에서 새 거래 가져오기:

`hledger import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/은행.csv</span>

- 두 파일에서 가져올 내용을 보여주고 아무 작업도 하지 않기:

`hledger import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/은행1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/은행2.csv</span>` --dry-run`

- 모든 CSV 파일에서 새 거래 가져오기, 모든 파일에 동일한 규칙 사용:

`hledger import --rules-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">common.rules</span>` *.csv`

- `bank.csv.rules`를 편집하면서 변환 오류 또는 결과 보기:

`watchexec -- hledger -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/은행.csv</span>` print`

- `bank.csv`의 현재 데이터를 이미 가져온 것으로 표시:

`hledger import --catchup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/은행.csv</span>

- `bank.csv`를 모두 새로 가져온 것으로 표시:

`rm -f .latest.bank.csv`
