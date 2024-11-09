---
layout: page
title: common/transcrypt (한국어)
description: "Git 저장소 내에서 파일을 투명하게 암호화."
content_hash: 36f02637f5cc4af55c32fd0376d1f67b7179b9ec
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transcrypt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transcrypt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transcrypt

Git 저장소 내에서 파일을 투명하게 암호화.
더 많은 정보: <https://github.com/elasticdog/transcrypt>.

- 구성되지 않은 저장소 초기화:

`transcrypt`

- 현재 암호화된 파일 나열:

`git ls-crypt`

- 구성된 저장소의 자격 증명 표시:

`transcrypt --display`

- 구성된 저장소의 새 클론을 초기화하고 복호화:

`transcrypt --cipher=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호화_알고리즘</span>

- 암호화 알고리즘이나 암호를 변경하기 위한 키 재설정:

`transcrypt --rekey`
