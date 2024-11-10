---
layout: page
title: linux/rpmbuild (한국어)
description: "RPM 패키지 빌드 도구."
content_hash: 5a11fd2432f96e6482f545da5f9652466e6fb7ee
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rpmbuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpmbuild

RPM 패키지 빌드 도구.
더 많은 정보: <https://manned.org/rpmbuild>.

- 바이너리 및 소스 패키지 빌드:

`rpmbuild -ba `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/spec_파일</span>

- 소스 패키지 없이 바이너리 패키지 빌드:

`rpmbuild -bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/spec_파일</span>

- 패키지를 빌드할 때 추가 변수 지정:

`rpmbuild -bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/spec_파일</span>` --define "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값1</span>`" --define "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값2</span>`"`
