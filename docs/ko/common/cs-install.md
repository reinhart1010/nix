---
layout: page
title: common/cs-install (한국어)
description: "`cs`를 설치할 때 구성된 디렉터리에 애플리케이션 설치 (바이너리를 로드하려면 `.bash_profile`에 `$ eval \"$(cs install --env)\"` 명령을 추가)."
content_hash: 50737e95f0296937e79fb1eb44998462e0fb3951
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cs-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cs-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cs install

`cs`를 설치할 때 구성된 디렉터리에 애플리케이션 설치 (바이너리를 로드하려면 `.bash_profile`에 `$ eval "$(cs install --env)"` 명령을 추가).
더 많은 정보: <https://get-coursier.io/docs/cli-install>.

- 특정 애플리케이션 설치:

`cs install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 특정 버전의 애플리케이션을 설치:

`cs install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_버전</span>

- 특정 이름으로 애플리케이션 검색:

`cs search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">부분_애플리케이션_이름</span>

- 가능한 경우 특정 애플리케이션을 업데이트:

`cs update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 설치된 모든 애플리케이션을 업데이트:

`cs update`

- 특정 애플리케이션 제거:

`cs uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 설치된 모든 애플리케이션 나열:

`cs list`

- 설치된 애플리케이션에 특정 Java 옵션을 전달:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...</span>
