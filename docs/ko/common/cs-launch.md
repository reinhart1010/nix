---
layout: page
title: common/cs-launch (한국어)
description: "설치할 필요 없이 Maven 종속성에서 직접 이름으로 애플리케이션을 실행."
content_hash: b1a44a0d828f0fc4b08d22258d4b7d1ea5a74de3
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cs-launch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cs-launch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cs launch

설치할 필요 없이 Maven 종속성에서 직접 이름으로 애플리케이션을 실행.
더 많은 정보: <https://get-coursier.io/docs/cli-launch>.

- 인수를 사용하여 특정 애플리케이션을 시작:

`cs launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 인수를 사용하여 특정 애플리케이션 버전을 시작:

`cs launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_버전</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 주요 파일이 무엇인지 지정하는 애플리케이션의 특정 버전인 specLaunch를 실행, 인수를 사용하여 특정 애플리케이션 버전을 지정:

`cs launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_버전</span>` --main-class `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메인_클래스_파일</span>

- 특정 Java 옵션 및 JVM 메모리 옵션을 사용하여 애플리케이션을 시작:

`cs launch --java-opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Doption_name1:option_value1 -Doption_name2:option_value2 ...</span>` --java-opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-Xjvm_option1 -Xjvm_option2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>
