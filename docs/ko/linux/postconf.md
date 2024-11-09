---
layout: page
title: linux/postconf (한국어)
description: "Postfix 구성 도구."
content_hash: bc10b6fd63364fcf91c2d016113915413f922cd8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/postconf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/postconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># postconf

Postfix 구성 도구.
이 명령은 기본적으로 `main.cf` 구성 매개변수의 값을 표시하고 잘못된 매개변수 이름에 대해 경고합니다. 또한 `main.cf` 구성 매개변수 값을 변경할 수 있습니다.
더 많은 정보: <https://manned.org/postconf>.

- 기본 구성 디렉토리 대신 `main.cf` 구성 파일의 디렉토리 지정:

`postconf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_디렉토리</span>

- `main.cf` 구성 파일을 편집하고 "name=value" 쌍으로 매개변수 설정 업데이트:

`postconf -e`

- 실제 설정 대신 `main.cf`의 기본 매개변수 설정 출력:

`postconf -d`

- 지정된 클래스의 매개변수만 표시. 클래스는 builtin, service, user 또는 all 중 하나일 수 있음:

`postconf -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스</span>

- Postfix SMTP 서버에서 사용 가능한 SASL 플러그인 유형 나열. 플러그인 유형은 `smtpd_sasl_type` 구성 매개변수로 `cyrus` 또는 `dovecot`을 이름으로 지정하여 선택:

`postconf -a`

- 지원되는 모든 조회 테이블 유형의 이름 나열. 조회 테이블은 구성 파일에서 `type:name`으로 지정되며, 유형으로 `btree`, `cdb`, `hash`, `mysql` 등이 있을 수 있음:

`postconf -m`
