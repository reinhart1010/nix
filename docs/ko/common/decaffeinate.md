---
layout: page
title: common/decaffeinate (한국어)
description: "CoffeeScript 소스를 최신 JavaScript로 이동."
content_hash: e22106c18741d53eb1eb16236c1e76910c7ccc31
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/decaffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/decaffeinate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# decaffeinate

CoffeeScript 소스를 최신 JavaScript로 이동.
더 많은 정보: <https://decaffeinate-project.org>.

- CoffeeScript 파일을 JavaScript로 변환:

`decaffeinate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.coffee</span>

- CoffeeScript v2 파일을 JavaScript로 변환:

`decaffeinate --use-cs2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.coffee</span>

- 가져오기 및 내보내기를 위해 require 및 `module.exports`를 변환:

`decaffeinate --use-js-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.coffee</span>

- 이름있는 내보내기를 허용하는 CoffeeScript를 변환:

`decaffeinate --loose-js-modules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.coffee</span>
