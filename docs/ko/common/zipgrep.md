---
layout: page
title: common/zipgrep (한국어)
description: "Zip 아카이브 내 파일에서 확장 정규 표현식을 사용하여 패턴 찾기 (`?`, `+`, `{}`, `()` 및 `|` 지원)."
content_hash: 42dacdf569e99ff187ba2348028ff815f0f41954
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zipgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zipgrep

Zip 아카이브 내 파일에서 확장 정규 표현식을 사용하여 패턴 찾기 (`?`, `+`, `{}`, `()` 및 `|` 지원).
더 많은 정보: <https://manned.org/zipgrep>.

- Zip 아카이브 내에서 패턴 검색:

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- 각 일치 항목에 대해 파일 이름과 줄 번호 출력:

`zipgrep -H -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- 패턴과 일치하지 않는 줄 검색:

`zipgrep -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- 검색에서 Zip 아카이브 내 파일 지정:

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색할/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색할/파일2</span>

- 검색에서 Zip 아카이브 내 파일 제외:

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제외할/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제외할/파일2</span>
