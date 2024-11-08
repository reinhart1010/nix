---
layout: page
title: common/phive (한국어)
description: "안전한 PHP 애플리케이션 배포를 위한 Phar 설치 및 검증 환경."
content_hash: c8536a49f0aff901f7cea6c0eb16e71f4ca6e809
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/phive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phive

안전한 PHP 애플리케이션 배포를 위한 Phar 설치 및 검증 환경.
더 많은 정보: <https://phar.io>.

- 사용 가능한 별칭이 있는 Phar 목록 표시:

`phive list`

- 지정한 Phar를 로컬 디렉터리에 설치:

`phive install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|url</span>

- 지정한 Phar를 전역적으로 설치:

`phive install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|url</span>` --global`

- 지정한 Phar를 대상 디렉터리에 설치:

`phive install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|url</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 Phar 파일을 최신 버전으로 업데이트:

`phive update`

- 지정한 Phar 파일 제거:

`phive remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭|url</span>

- 사용하지 않는 Phar 파일 제거:

`phive purge`

- 사용 가능한 모든 명령 나열:

`phive help`
