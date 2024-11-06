---
layout: page
title: common/phpmd (한국어)
description: "PHP Mess Detector: 일반적인 잠재적 문제를 확인."
content_hash: 0ec91d3f9e1984cf98111eacad268c88acf8ad08
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/phpmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpmd

PHP Mess Detector: 일반적인 잠재적 문제를 확인.
더 많은 정보: <https://github.com/phpmd/phpmd>.

- 사용 가능한 규칙 세트 및 형식 목록 표시:

`phpmd`

- 쉼표로 구분된 규칙 세트를 사용하여 파일 또는 폴더에서 문제 스캔:

`phpmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙세트1,규칙세트2,...</span>

- 규칙의 최소 우선순위 임계값 지정:

`phpmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙세트1,규칙세트2,...</span>` --minimumpriority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">우선순위</span>

- 분석에 포함할 확장자 지정:

`phpmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙세트1,규칙세트2,...</span>` --suffixes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장자</span>

- 쉼표로 구분된 특정 폴더 제외:

`phpmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1,경로/대상/파일_또는_폴더2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙세트1,규칙세트2,...</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더_패턴</span>

- 결과를 `stdout` 대신 파일에 출력:

`phpmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙세트1,규칙세트2,...</span>` --reportfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/보고서_파일</span>

- 경고 억제 PHPDoc 주석 사용 무시:

`phpmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xml|text|html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙세트1,규칙세트2,...</span>` --strict`
