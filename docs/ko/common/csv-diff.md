---
layout: page
title: common/csv-diff (한국어)
description: "두 개의 CSV, TSV 또는 JSON 파일 간의 차이점을 확인."
content_hash: 27cfe996313e616f63cca489b5d6fef54a0585c0
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/csv-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csv-diff

두 개의 CSV, TSV 또는 JSON 파일 간의 차이점을 확인.
더 많은 정보: <https://github.com/simonw/csv-diff>.

- 특정 열을 고유 식별자로 사용해 파일 간의 차이점을 사람이 읽을 수 있는 요약정보로 표시:

`csv-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.csv</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_이름</span>

- 최소한 하나의 변경 사항이 있는 행의 변경되지 않은 값은 포함하는 파일 간의 차이점에 대해서, 사람이 읽을 수 있는 요약정보로 표시:

`csv-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.csv</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_이름</span>` --show-unchanged`

- 특정 열을 고유 식별자로 사용하여 JSON 형식 파일 간 차이점을 요약정보로 표시:

`csv-diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.csv</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_이름</span>` --json`
