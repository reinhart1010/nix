---
layout: page
title: common/phpunit (한국어)
description: "PHPUnit 명령줄 테스트 실행기."
content_hash: 52105d570201b1353c4185d9962ba63cbca18e01
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/phpunit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpunit

PHPUnit 명령줄 테스트 실행기.
더 많은 정보: <https://phpunit.de>.

- 현재 디렉토리에서 테스트 실행. 참고: 'phpunit.xml' 파일이 존재해야 합니다:

`phpunit`

- 특정 파일에서 테스트 실행:

`phpunit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/TestFile.php</span>

- 주어진 그룹으로 주석이 달린 테스트 실행:

`phpunit --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 테스트를 실행하고 HTML 형식의 커버리지 보고서 생성:

`phpunit --coverage-html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
