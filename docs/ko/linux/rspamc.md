---
layout: page
title: linux/rspamc (한국어)
description: "rspamd 서버용 커맨드라인 클라이언트."
content_hash: b03724908bb8404dcdb3fe328d9441c82f3b2160
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rspamc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rspamc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rspamc

rspamd 서버용 커맨드라인 클라이언트.
더 많은 정보: <https://manned.org/rspamc>.

- 베이지안 필터를 훈련시켜 이메일을 스팸으로 인식:

`rspamc learn_spam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이메일_파일</span>

- 베이지안 필터를 훈련시켜 이메일을 정상 메일로 인식:

`rspamc learn_ham `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이메일_파일</span>

- 이메일에 대한 수동 보고서 생성:

`rspamc symbols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이메일_파일</span>

- 서버 통계 표시:

`rspamc stat`
