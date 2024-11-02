---
layout: page
title: common/wp (한국어)
description: "WordPress 인스턴스를 관리하는 공식 명령줄 인터페이스."
content_hash: fe1cbf3578e510259570944b36da1469bba05acf
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wp

WordPress 인스턴스를 관리하는 공식 명령줄 인터페이스.
더 많은 정보: <https://wp-cli.org/>.

- 운영 체제, 셸, PHP 및 WP-CLI(`wp`) 설치 정보 출력:

`wp --info`

- WP-CLI 업데이트:

`wp cli update`

- 현재 디렉토리에 새로운 WordPress 설치 파일 다운로드, 필요시 로케일 지정:

`wp core download --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로케일</span>

- 기본 `wpconfig` 파일 생성 (데이터베이스가 `localhost`에 있다고 가정):

`wp config create --dbname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` --dbuser=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_사용자</span>` --dbpass=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_비밀번호</span>

- WordPress 플러그인 설치 및 활성화:

`wp plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인</span>` --activate`

- 데이터베이스에서 문자열의 모든 인스턴스 교체:

`wp search-replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기존_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_문자열</span>

- WordPress 확장 RSS(WXR) 파일의 내용 가져오기:

`wp import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.xml</span>
