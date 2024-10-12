---
layout: page
title: common/clj (한국어)
description: "REPL을 시작하거나 데이터로 함수를 호출하는 Clojure 도구."
content_hash: 9e4b59407c42d6420d7c50607bc538e5ad90eefb
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/clj.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clj.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clj.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clj

REPL을 시작하거나 데이터로 함수를 호출하는 Clojure 도구.
모든 옵션은 `deps.edn` 파일에서 정의할 수 있음.
더 많은 정보: <https://clojure.org/guides/deps_and_cli>.

- REPL를 시작 (대화형 쉘):

`clj`

- 함수의 실행:

`clj -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스/함수_이름</span>

- 지정된 네임스페이스의 기본 기능을 실행:

`clj -M -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>

- 의존성을 해결하고, 라이브러리를 다운로드하고, 클래스 경로를 생성/캐싱하여 프로젝트를 준비:

`clj -P`

- CIDER 미들웨어로 nREPL 서버를 시작:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}</span>`' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- ClojureScript용 REPL을 시작하고 웹 브라우저를 열기:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}</span>`' --main cljs.main --repl`
