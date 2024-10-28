---
layout: page
title: common/gox (한국어)
description: "Go 프로그램을 크로스 컴파일."
content_hash: 99c6aa53bd26ea3ff57e6bb840254e42672b6c76
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/common/gox.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gox

Go 프로그램을 크로스 컴파일.
더 많은 정보: <https://github.com/mitchellh/gox>.

- 모든 운영체제 및 아키텍처 조합에 대해 현재 디렉터리에서 Go 프로그램을 컴파일:

`gox`

- 원격 URL에서 Go 프로그램을 다운로드하고 컴파일:

`gox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_2</span>

- 특정 운영 체제에 대한 현재 디렉터리를 컴파일:

`gox -os="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">운영체제</span>`"`

- 단일 운영 체제 및 아키텍처 조합에 대한 현재 디렉터리를 컴파일:

`gox -osarch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">운영체제</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아키텍처</span>`"`
