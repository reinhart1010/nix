---
layout: page
title: common/imapsync (한국어)
description: "두 개의 IMAP 서버 사이에 중복없이 단방향으로 이메일 사서함을 동기화, 복사 및 마이그레이션하기 위한 이메일 IMAP 도구."
content_hash: 22dd43989a1208a6d00c314dde3c52acdc6d296f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/imapsync.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/imapsync.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># imapsync

두 개의 IMAP 서버 사이에 중복없이 단방향으로 이메일 사서함을 동기화, 복사 및 마이그레이션하기 위한 이메일 IMAP 도구.
더 많은 정보: <https://imapsync.lamiral.info>.

- 호스트1과 호스트2 간에 IMAP 계정을 동기화:

`imapsync --host1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트1</span>` --user1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자1</span>` --password1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀1</span>` --host2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트2</span>` --user2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자2</span>` --password2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀2</span>
