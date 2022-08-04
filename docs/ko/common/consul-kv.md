---
layout: page
title: common/consul-kv (한국어)
description: "서비스 검색 기능과 상태 확인을 위한 분산된 키-값(key-value)쌍 저장."
content_hash: 68af1865e1b7f1a4a410adfb6c4968718ea29093
related_topics:
  - title: English version
    url: /en/common/consul-kv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/consul-kv.html
    icon: bi bi-globe
---
# consul-kv

서비스 검색 기능과 상태 확인을 위한 분산된 키-값(key-value)쌍 저장.
더 많은 정보: <https://learn.hashicorp.com/consul/getting-started/kv>.

- 키-값(key-value)쌍으로 저장된 값 읽기:

`consul kv get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 새로운 키-값(key-value)쌍으로 저장:

`consul kv put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 키-값(key-value)쌍 제거:

`consul kv delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>
