---
layout: page
title: common/gcloud-config-set (한국어)
description: "Google Cloud CLI 구성에서 속성을 설정."
content_hash: 677699f1f74628762650d2238e5e97037e78908c
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gcloud-config-set.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-config-set.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud config set

Google Cloud CLI 구성에서 속성을 설정.
속성은 Google Cloud CLI 동작의 다양한 측면을 제어합니다.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/config/set>.

- core 섹션에서 프로젝트 속성 설정:

`gcloud config set project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_ID</span>

- 향후 작업을 위한 컴퓨트 영역 설정:

`gcloud config set compute/zone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">존_이름</span>

- 스크립팅에 적합하도록 gcloud의 프롬프트 비활성화:

`gcloud config set disable_prompts true`

- 현재 사용 중인 속성 목록 보기:

`gcloud config list`

- 설정된 속성 해제:

`gcloud config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>

- 새로운 구성 프로필 생성:

`gcloud config configurations create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>

- 다른 구성 프로필 간 전환:

`gcloud config configurations activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>
