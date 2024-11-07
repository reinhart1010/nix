---
layout: page
title: common/plocate (한국어)
description: "파일 이름을 빠르게 찾기."
content_hash: e554b46ca10f40d20c52774338f99ffb94088739
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/plocate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/plocate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># plocate

파일 이름을 빠르게 찾기.
새 파일을 포함하려면 `sudo updatedb`를 실행하세요.
더 많은 정보: <https://plocate.sesse.net>.

- 데이터베이스에서 패턴 검색 (주기적으로 재계산):

`plocate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 정확한 파일 이름으로 파일 검색 (글로벌 문자가 포함되지 않은 패턴은 `*패턴*`으로 해석됨):

`plocate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>
