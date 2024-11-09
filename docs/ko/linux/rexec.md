---
layout: page
title: linux/rexec (한국어)
description: "원격 호스트에서 명령을 실행합니다."
content_hash: b72d2c2dd912292aa75d4f64ff1dc9db56c913b7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rexec.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/rexec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rexec

원격 호스트에서 명령을 실행합니다.
참고: `rexec`는 데이터를 일반 텍스트로 전송하므로 주의해서 사용하세요. 암호화된 통신을 위해 SSH와 같은 보안 대안을 고려하세요.
더 많은 정보: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- 원격 [h]호스트에서 명령 실행:

`rexec -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- 원격 [h]호스트에서 원격 [u]사용자명을 지정:

`rexec -username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux</span>

- 원격 [h]호스트에서 `stdin`을 `/dev/null`로 리디렉션:

`rexec --no-err -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- 원격 [h]호스트에서 원격 [P]포트를 지정:

`rexec -P=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
