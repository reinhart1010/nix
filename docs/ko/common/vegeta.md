---
layout: page
title: common/vegeta (한국어)
description: "HTTP 부하 테스트를 위한 명령줄 도구 및 라이브러리."
content_hash: f3098cc299f570bbacb312d734aeceddc4595828
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vegeta.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vegeta.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vegeta

HTTP 부하 테스트를 위한 명령줄 도구 및 라이브러리.
같이 보기: `ab`.
더 많은 정보: <https://github.com/tsenart/vegeta>.

- 30초 동안 공격 시작:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>

- 자체 서명된 HTTPS 인증서가 있는 서버에 대한 공격 시작:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -insecure -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>

- 초당 10개의 요청 비율로 공격 시작:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` -rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 공격을 시작하고 보고서 표시:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` | vegeta report`

- 공격을 시작하고 결과를 그래프에 플롯(시간에 따른 지연):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET https://example.com</span>`" | vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` | vegeta plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.html</span>

- 파일에 있는 여러 URL에 대한 공격 시작:

`vegeta attack -duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30s</span>` -targets=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requests.txt</span>` | vegeta report`
