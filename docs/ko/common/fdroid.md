---
layout: page
title: common/fdroid (한국어)
description: "F-Droid 빌드 도구."
content_hash: 12de480489157c528627d0141388043cb9b8043f
last_modified_at: 2024-10-21
related_topics:
  - title: Deutsch version
    url: /de/common/fdroid.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fdroid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdroid

F-Droid 빌드 도구.
F-Droid는 Android 플랫폼용 FOSS (무료 및 오픈 소스 소프트웨어) 애플리케이션의 설치 가능한 카탈로그.
더 많은 정보: <https://f-droid.org/>.

- 특정 앱 구축:

`fdroid build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 빌드 서버 VM에서 특정 앱을 빌드:

`fdroid build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>` --server`

- 앱을 로컬 저장소에 게시:

`fdroid publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 연결된 모든 기기에 앱을 설치:

`fdroid install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 메타데이터의 형식이 올바른지 확인:

`fdroid lint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 자동으로 서식을 수정 (가능한 경우):

`fdroid rewritemeta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>
