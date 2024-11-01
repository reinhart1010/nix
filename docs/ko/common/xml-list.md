---
layout: page
title: common/xml-list (한국어)
description: "디렉토리의 내용을 XML 형식으로 나열 (예: `ls`)."
content_hash: e281f29fc7cde0fdab879b2cbb71ad6a6c94cab3
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/xml-list.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xml-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xml list

디렉토리의 내용을 XML 형식으로 나열 (예: `ls`).
더 많은 정보: <https://xmlstar.sourceforge.net/docs.php>.

- 현재 디렉토리의 목록을 XML 문서로 작성:

`xml list > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리_목록.xml</span>

- 지정된 디렉토리의 목록을 XML 문서로 작성:

`xml list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리_목록.xml</span>

- 도움말 표시:

`xml list --help`
