---
layout: page
title: common/offlineimap (한국어)
description: "원격 IMAP 서버를 로컬 Maildir 폴더와 동기화."
content_hash: da44a115c1d74f7624956589ce31e07dee1a1eac
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/offlineimap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/offlineimap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># offlineimap

원격 IMAP 서버를 로컬 Maildir 폴더와 동기화.
더 많은 정보: <https://www.offlineimap.org>.

- 자동 새로 고침 없이 한 번 동기화:

`offlineimap -o`

- 특정 계정 동기화:

`offlineimap -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정</span>

- 특정 폴더 동기화:

`offlineimap -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폴더</span>
