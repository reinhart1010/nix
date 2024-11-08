---
layout: page
title: linux/chpasswd (한국어)
description: "여러 사용자의 비밀번호를 `stdin`을 통해 변경합니다."
content_hash: cc923addef8ff5199ad8ff76b23d5c25ff4b55b4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/chpasswd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chpasswd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpasswd

여러 사용자의 비밀번호를 `stdin`을 통해 변경합니다.
더 많은 정보: <https://manned.org/chpasswd.8>.

- 특정 사용자의 비밀번호 변경:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_비밀번호</span>`" | sudo chpasswd`

- 여러 사용자의 비밀번호 변경 (입력 텍스트에는 공백이 없어야 합니다.):

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명_1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_비밀번호_1</span>`\n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명_2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_비밀번호_2</span>`" | sudo chpasswd`

- 특정 사용자의 비밀번호를 암호화된 형태로 변경:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_암호화된_비밀번호</span>`" | sudo chpasswd --encrypted`

- 특정 사용자의 비밀번호를 변경하고 저장된 비밀번호에 특정 암호화를 사용:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_비밀번호</span>`" | sudo chpasswd --crypt-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NONE|DES|MD5|SHA256|SHA512</span>
