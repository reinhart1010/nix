---
layout: page
title: common/idnits (한국어)
description: "제출 니트에 대한 인터넷 초안을 확인."
content_hash: 911d895ec95a5fb081c1dfc66df99bef90a58c46
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/idnits.html
    icon: bi bi-globe
tldri18n_status: 2
---
# idnits

제출 니트에 대한 인터넷 초안을 확인.
<https://www.ietf.org/id-info/checklist>에 나열된 요구 사항의 섹션 2.1 및 2.2에 대한 위반 사항을 찾음.
더 많은 정보: <https://github.com/ietf-tools/idnits>.

- 파일에서 니트를 확인:

`idnits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 표시하지 않고 니트 수 계산:

`idnits --nitcount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 위반 라인에 대한 추가 정보 표시:

`idnits --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 현재 연도 대신 상용구에 지정된 연도를 예상:

`idnits --year `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 문서가 지정된 상태에 있다고 가정:

`idnits --doctype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|informational|experimental|bcp|ps|ds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>
