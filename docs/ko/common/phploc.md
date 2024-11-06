---
layout: page
title: common/phploc (한국어)
description: "PHP 프로젝트의 크기를 빠르게 측정하고 구조를 분석합니다."
content_hash: ec7017fde4b277cc26c2bf9f17453cc4665d48a9
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/phploc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phploc

PHP 프로젝트의 크기를 빠르게 측정하고 구조를 분석합니다.
더 많은 정보: <https://github.com/sebastianbergmann/phploc>.

- 디렉터리를 분석하고 결과 출력:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 쉼표로 구분된 파일 목록에서 특정 파일만 포함 (글로벌 패턴 사용 가능):

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --names '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1,경로/대상/파일2,...</span>`'`

- 쉼표로 구분된 파일 목록에서 특정 파일 제외 (글로벌 패턴 사용 가능):

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --names-exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1,경로/대상/파일2,...</span>`'`

- 특정 디렉터리를 분석에서 제외:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/제외_폴더</span>

- 결과를 특정 CSV 파일에 기록:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --log-csv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 결과를 특정 XML 파일에 기록:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --log-xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- PHPUnit 테스트 케이스 클래스와 테스트 메서드 개수 세기:

`phploc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --count-tests`
