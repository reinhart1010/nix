---
layout: page
title: common/msmtp (한국어)
description: "SMTP 클라이언트."
content_hash: 01a423a50ede53a9f797d450991222ca092562d9
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/msmtp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/msmtp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msmtp

SMTP 클라이언트.
`stdin`에서 텍스트를 읽고 이를 SMTP 서버로 전송합니다.
더 많은 정보: <https://marlam.de/msmtp>.

- `~/.msmtprc`에 설정된 기본 계정을 사용하여 이메일 전송:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">안녕하세요</span>`" | msmtp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to@example.org</span>

- `~/.msmtprc`에 설정된 특정 계정을 사용하여 이메일 전송:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">안녕하세요</span>`" | msmtp --account=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to@example.org</span>

- 설정된 계정 없이 이메일 전송. 비밀번호는 `~/.msmtprc` 파일에 명시해야 합니다:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">안녕하세요</span>`" | msmtp --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">999</span>` --from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from@example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to@example.org</span>
