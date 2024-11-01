---
layout: page
title: common/tlmgr-pinning (한국어)
description: "고정 작업은 고정 파일을 관리합니다."
content_hash: 7f9851754ab859fb8e8286434c094e9761075d75
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-pinning.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-pinning.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr pinning

고정 작업은 고정 파일을 관리합니다.
더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

- 현재 고정 데이터를 표시:

`tlmgr pinning show`

- 일치하는 패키지를 주어진 저장소에 고정:

`tlmgr pinning add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 주어진 저장소에 대해 고정 파일에 기록된 패키지를 제거:

`tlmgr pinning remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- 주어진 저장소의 모든 고정 데이터 제거:

`tlmgr pinning remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` --all`
