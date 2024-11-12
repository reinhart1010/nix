---
layout: page
title: osx/emond (한국어)
description: "다양한 서비스로부터 이벤트를 수신하고, 간단한 규칙 엔진을 통해 처리하여 동작을 수행하는 이벤트 모니터 서비스."
content_hash: 9810953703ec3170d94189e744c505e6056a395d
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/emond.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/emond.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/emond.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emond

다양한 서비스로부터 이벤트를 수신하고, 간단한 규칙 엔진을 통해 처리하여 동작을 수행하는 이벤트 모니터 서비스.
동작은 명령 실행, 이메일 전송 또는 SMS 메시지 발송을 포함할 수 있습니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/emond.8.html>.

- 데몬 시작:

`emond`

- emond가 처리할 규칙을 파일 또는 디렉토리 경로로 지정:

`emond -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 특정 설정 파일 사용:

`emond -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정_파일</span>
