---
layout: page
title: common/git-credential (한국어)
description: "사용자 자격 증명을 검색하고 저장."
content_hash: 08ed16a4a992bb7332ff52aac2d23b34cdf9f00f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-credential.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-credential.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-credential.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git credential

사용자 자격 증명을 검색하고 저장.
더 많은 정보: <https://git-scm.com/docs/git-credential>.

- 자격 증명 정보를 표시하고, 구성 파일에서 사용자 명과 비밀번호를 검색:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential fill`

- 모든 구성된 자격 증명 도우미에 자격 증명 정보를 보내서 나중에 사용할 수 있도록 저장:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential approve`

- 모든 구성된 자격 증명 도우미에서 지정된 자격 증명 정보를 삭제:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential reject`
