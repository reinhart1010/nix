---
layout: page
title: common/vale (한국어)
description: "Markdown 및 AsciiDoc과 같은 여러 마크업 형식을 지원하는 확장 가능한 스타일 검사기."
content_hash: 968e3625cc1ec4110d3c50419c396d1fdad0adc6
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vale.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vale

Markdown 및 AsciiDoc과 같은 여러 마크업 형식을 지원하는 확장 가능한 스타일 검사기.
더 많은 정보: <https://vale.sh>.

- 파일의 스타일 검사:

`vale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정된 설정 파일을 사용하여 파일의 스타일 검사:

`vale --config='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/.vale.ini</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 결과를 JSON 형식으로 출력:

`vale --output=JSON `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 심각도 이상의 스타일 문제 검사:

`vale --minAlertLevel=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suggestion|warning|error</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 스타일 검사, 마크업 형식 지정:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.md</span>` | vale --ext=.md`

- 현재 설정 나열:

`vale ls-config`
