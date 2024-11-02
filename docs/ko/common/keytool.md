---
layout: page
title: common/keytool (한국어)
description: "Java에 포함된 인증서 관리 도구."
content_hash: ac7be8cd43f501a4f5c7fde5db9f46499d7f6b1f
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/keytool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/keytool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># keytool

Java에 포함된 인증서 관리 도구.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/keytool.html>.

- 키스토어 생성:

`keytool -genkeypair -v -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.keystore</span>` -alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>

- 키스토어 비밀번호 변경:

`keytool -storepasswd -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.keystore</span>

- 특정 키스토어 내 키의 비밀번호 변경:

`keytool -keypasswd -alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` -keystore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.keystore</span>
