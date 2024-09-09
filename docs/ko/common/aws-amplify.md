---
layout: page
title: common/aws-amplify (한국어)
description: "안전하고, 확장 가능한 모바일 및 웹 애플리케이션을 구축하기 위한 개발 플랫폼."
content_hash: 0c5c6aa1a199f3204782d999b116b55214688e75
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/aws-amplify.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-amplify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-amplify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws amplify

안전하고, 확장 가능한 모바일 및 웹 애플리케이션을 구축하기 위한 개발 플랫폼.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>.

- 새로운 Amplify 앱 생성:

`aws amplify create-app --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세부정보</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>` --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랫폼</span>` --environment-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경_변수</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 기존 Amplify 앱 삭제:

`aws amplify delete-app --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 특정 Amplify 앱 세부정보 가져오기:

`aws amplify get-app --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 모든 Amplify 앱 나열:

`aws amplify list-apps`

- Amplify 앱 설정 업데이트:

`aws amplify update-app --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_이름</span>` --description `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_세부정보</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_레포지토리_주소</span>` --environment-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_환경_변수</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_태그</span>

- Amplify 앱에 새로운 백엔드 환경 추가:

`aws amplify create-backend-environment --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>` --environment-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경변수_이름</span>` --deployment-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artifacts</span>

- Amplify 앱에서 백엔드 환경 제거:

`aws amplify delete-backend-environment --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>` --environment-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경변수_이름</span>

- Amplify 앱의 모든 백엔드 환경 나열:

`aws amplify list-backend-environments --app-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>
