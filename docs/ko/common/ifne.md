---
layout: page
title: common/ifne (한국어)
description: "`stdin`의 비어 있음에 따라 명령을 실행."
content_hash: 1c7dd4d7984128a3e75472bafbc2ae0304ce0a4f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ifne.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ifne.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ifne

`stdin`의 비어 있음에 따라 명령을 실행.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- `stdin`이 비어 있지 않은 경우에만 지정된 명령을 실행:

`ifne `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 옵션 ...</span>

- `stdin`이 비어 있는 경우에만 지정된 명령을 실행하고, 그렇지 않으면 `stdin`을 `stdout`에 전달:

`ifne -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어 옵션 ...</span>
