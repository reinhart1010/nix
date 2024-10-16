---
layout: page
title: common/ern (한국어)
description: "전극 네이티브 플랫폼 명령줄 클라이언트."
content_hash: 9adc2092f267841b7df80b5e01f5f256785ae946
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/ern.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ern.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ern

전극 네이티브 플랫폼 명령줄 클라이언트.
더 많은 정보: <https://native.electrode.io/reference/index-6>.

- 새로운 `ern` 애플리케이션(`MiniApp`)을 생성:

`ern create-miniapp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- iOS/Android 러너 애플리케이션에서 하나 이상의 `MiniApps`를 실행:

`ern run-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ios|android</span>

- 전극 네이티브 컨테이너 만들기:

`ern create-container --miniapps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/miniapp_디렉토리</span>` --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ios|android</span>

- 전극 네이티브 컨테이너를 로컬 Maven 저장소에 저장:

`ern publish-container --publisher `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maven</span>` --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android</span>` --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"groupId":"com.walmart.ern","artifactId":"quickstart"}'</span>

- iOS 컨테이너를 사전 컴파일된 바이너리 프레임워크로 변환:

`ern transform-container --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ios</span>` --transformer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xcframework</span>

- 설치된 모든 전극 Native 버전을 나열:

`ern platform versions`

- 로깅 수준을 설정:

`ern platform config set logLevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace|debug</span>
