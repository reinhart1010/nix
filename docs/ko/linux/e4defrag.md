---
layout: page
title: linux/e4defrag (한국어)
description: "ext4 파일 시스템을 조각 모음합니다."
content_hash: 69d072179f977039a9e36a9dba28570a5a09233f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/e4defrag.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/e4defrag.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># e4defrag

ext4 파일 시스템을 조각 모음합니다.
더 많은 정보: <https://manned.org/e4defrag>.

- 파일 시스템 조각 모음:

`e4defrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템이 얼마나 조각화되었는지 확인:

`e4defrag -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 오류와 각 파일의 조각화 개수를 조각 모음 전후에 출력:

`e4defrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
