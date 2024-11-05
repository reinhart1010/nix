---
layout: page
title: common/php-coveralls (한국어)
description: "Coveralls를 위한 PHP 클라이언트."
content_hash: 16366b2de217c640a3e9ecd7ca5c769e6ec4e0ea
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/php-coveralls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/php-coveralls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># php-coveralls

Coveralls를 위한 PHP 클라이언트.
더 많은 정보: <https://php-coveralls.github.io/php-coveralls>.

- Coveralls에 커버리지 정보를 전송:

`php-coveralls`

- 특정 디렉토리에 대한 커버리지 정보를 Coveralls에 전송:

`php-coveralls --root_dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 설정 파일을 사용하여 Coveralls에 커버리지 정보를 전송:

`php-coveralls --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/.coveralls.yml</span>

- 자세한 출력과 함께 Coveralls에 커버리지 정보를 전송:

`php-coveralls --verbose`

- 실행 가능한 문장이 없는 소스 파일을 제외하고 Coveralls에 커버리지 정보를 전송:

`php-coveralls --exclude-no-stmt`

- 특정 환경 이름을 사용하여 Coveralls에 커버리지 정보를 전송:

`php-coveralls --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test|dev|prod</span>

- 여러 Coverage Clover XML 파일을 업로드하도록 지정:

`php-coveralls --coverage_clover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첫번째_clover.xml</span>` --coverage_clover `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/두번째_clover.xml</span>

- Coveralls에 전송될 JSON을 특정 파일로 출력:

`php-coveralls --json_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/coveralls-전송.json</span>
