---
layout: page
title: common/cf (한국어)
description: "Cloud Foundry에서 앱과 서비스를 관리."
content_hash: 09dc66a356aad02eca9da408b7a6ab1013e38809
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/cf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cf

Cloud Foundry에서 앱과 서비스를 관리.
더 많은 정보: <https://docs.cloudfoundry.org>.

- Cloud Foundry API에 로그인:

`cf login -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_주소</span>

- 기본 설정을 사용하여 앱을 푸시:

`cf push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 조직에서 사용할 수 있는 서비스 보기:

`cf marketplace`

- 서비스 인스턴스를 생성:

`cf create-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랜</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 애플리케이션을 서비스에 연결:

`cf bind-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>

- 코드가 앱에 포함되어 있지만, 독립적으로 실행되는 스크립트를 실행:

`cf run-task `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트_명령어</span>`" --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 앱을 호스팅하는 VM으로 대화형 SSH 세션을 시작:

`cf ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 최근 앱 로그 덤프 보기:

`cf logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>` --recent`
