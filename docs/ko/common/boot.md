---
layout: page
title: common/boot (한국어)
description: "Clojure 프로그래밍 언어를 위한 빌드."
content_hash: e9bda610c62e238d3ad56a39dca834d183204f97
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/boot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/boot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# boot

Clojure 프로그래밍 언어를 위한 빌드.
더 많은 정보: <https://github.com/boot-clj/boot>.

- 프로젝트 혹은 독립으로 REPL 세션 시작:

`boot repl`

- 단일 "uberjar" 구축:

`boot jar`

- 명령어 안내:

`boot cljs --help`

- 템플릿을 기반으로 새로운 프로젝트에 대한 기반 생성:

`boot --dependencies boot/new new --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿명</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트명</span>

- 개발용 빌드 (부트/새 템플릿을 사용하는 경우):

`boot dev`

- 생산용 빌드 (부트/새 템플릿을 사용하는 경우):

`boot prod`
