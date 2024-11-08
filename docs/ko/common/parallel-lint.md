---
layout: page
title: common/parallel-lint (한국어)
description: "PHP 파일의 구문을 병렬로 검사."
content_hash: d0749e16fdfc29fdc7cda0337c130ab4fb2b3b7e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/parallel-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# parallel-lint

PHP 파일의 구문을 병렬로 검사.
더 많은 정보: <https://github.com/JakubOnderka/PHP-Parallel-Lint>.

- 특정 디렉토리의 구문 검사:

`parallel-lint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 지정된 병렬 프로세스 수를 사용하여 디렉토리 구문 검사:

`parallel-lint -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 디렉토리를 제외하고 디렉토리 구문 검사:

`parallel-lint --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/제외_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 쉼표로 구분된 확장자 목록을 사용하여 파일 디렉토리의 구문 검사:

`parallel-lint -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php,html,phpt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉토리의 구문 검사를 수행하고 결과를 JSON으로 출력:

`parallel-lint --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 디렉토리의 구문 검사를 수행하고 오류가 있는 행에 대한 Git Blame 결과 표시:

`parallel-lint --blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
