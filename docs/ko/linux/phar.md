---
layout: page
title: linux/phar (한국어)
description: "PHP 아카이브(PHAR)를 생성, 업데이트 또는 추출."
content_hash: b1eefb5d3096373aa5da4e10d6e59723bbb7588e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/phar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phar

PHP 아카이브(PHAR)를 생성, 업데이트 또는 추출.
더 많은 정보: <https://manned.org/phar>.

- 하나 이상의 파일이나 디렉터리를 Phar 파일에 추가:

`phar add -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리1 경로/대상/파일_또는_디렉터리2 ...</span>

- Phar 파일의 내용 표시:

`phar list -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>

- Phar 파일에서 지정된 파일이나 디렉터리 삭제:

`phar delete -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_디렉터리</span>

- Phar 파일 내 파일과 디렉터리 압축 또는 압축 해제:

`phar compress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알고리즘</span>

- Phar 파일에 대한 정보 얻기:

`phar info -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>

- 특정 해시 알고리즘으로 Phar 파일 서명:

`phar sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알고리즘</span>

- OpenSSL 개인 키로 Phar 파일 서명:

`phar sign -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/phar_파일</span>` -h openssl -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>

- 도움말 및 사용 가능한 해싱/압축 알고리즘 표시:

`phar help`
