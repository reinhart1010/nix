---
layout: page
title: common/subfinder (한국어)
description: "웹사이트의 유효한 하위 도메인을 발견."
content_hash: f149434a5494449ebf9953bb98d53f34880748ea
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/subfinder.html
    icon: bi bi-globe
tldri18n_status: 2
---
# subfinder

웹사이트의 유효한 하위 도메인을 발견.
버그 바운티에 유용하고 침투 테스트에 안전하도록 설계된 패시브 프레임워크.
더 많은 정보: <https://github.com/projectdiscovery/subfinder>.

- 특정 [d] 도메인의 하위 도메인 찾기:

`subfinder -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 발견된 하위 도메인만 표시:

`subfinder -silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 활성 하위 도메인만 표시:

`subfinder -nW -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 모든 소스를 사용하여 열거:

`subfinder -all -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 쉼표로 구분된 [r] 리졸버 목록 사용:

`subfinder -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8,1.1.1.1,...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
