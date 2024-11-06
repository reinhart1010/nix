---
layout: page
title: common/phpcpd (한국어)
description: "PHP 코드의 복사 및 붙여넣기 감지기."
content_hash: 5e500ffb5bf14e44bdf8a9d3cd3fc1cbedb3c841
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/phpcpd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpcpd

PHP 코드의 복사 및 붙여넣기 감지기.
더 많은 정보: <https://github.com/sebastianbergmann/phpcpd>.

- 특정 파일이나 디렉터리에 대해 중복된 코드 분석:

`phpcpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 변수 이름에 대한 퍼지 매칭을 사용하여 분석:

`phpcpd --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 최소 동일한 라인 수 지정 (기본값은 5):

`phpcpd --min-lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라인_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 최소 동일한 토큰 수 지정 (기본값은 70):

`phpcpd --min-tokens `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 분석에서 디렉터리 제외 (소스에 상대적이어야 함):

`phpcpd --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/제외_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 결과를 PHP-CPD XML 파일로 출력:

`phpcpd --log-pmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/로그_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>
