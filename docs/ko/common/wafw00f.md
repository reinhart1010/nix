---
layout: page
title: common/wafw00f (한국어)
description: "웹 애플리케이션 방화벽(WAF) 제품을 식별하고 지문을 채취하여 사이트를 보호."
content_hash: 1b888e6d0ba3125ebe0ce409915d37d481b3ab16
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wafw00f.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wafw00f.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wafw00f

웹 애플리케이션 방화벽(WAF) 제품을 식별하고 지문을 채취하여 사이트를 보호.
더 많은 정보: <https://github.com/EnableSecurity/wafw00f>.

- 웹사이트가 WAF를 사용 중인지 확인:

`wafw00f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- 첫 번째 일치 항목에서 멈추지 않고 감지 가능한 모든 WAF 테스트:

`wafw00f --findall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- 요청을 프록시(예: BurpSuite)를 통해 전달:

`wafw00f --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- 특정 WAF 제품 테스트 (`wafw00f -l`을 실행하여 지원되는 모든 WAF 목록 확인):

`wafw00f --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Cloudflare|Cloudfront|Fastly|ZScaler|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- 파일에서 사용자 지정 헤더 전달:

`wafw00f --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/헤더.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.example.com</span>

- 파일에서 대상 입력을 읽고 자세한 출력 표시 (더 많은 자세한 출력을 위해 `v`를 여러 번 사용):

`wafw00f --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/urls.txt</span>` -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v</span>

- 감지 가능한 모든 WAF 나열:

`wafw00f --list`
