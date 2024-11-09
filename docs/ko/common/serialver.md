---
layout: page
title: common/serialver (한국어)
description: "클래스의 serialVersionUID를 반환."
content_hash: 7546d68012a29af17f975441bfeacfc6946d38fb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/serialver.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/serialver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># serialver

클래스의 serialVersionUID를 반환.
기본적으로 보안 관리자를 설정하지 않습니다.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/serialver.html>.

- 클래스의 serialVersionUID 표시:

`serialver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스_이름들</span>

- 콜론으로 구분된 클래스 및 리소스 목록의 serialVersionUID 표시:

`serialver -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스_이름1:클래스_이름2:...</span>

- Java 애플리케이션 런처의 참조 페이지에서 Java 가상 머신으로 특정 옵션 사용:

`serialver -Joption `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스_이름들</span>
