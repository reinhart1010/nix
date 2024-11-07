---
layout: page
title: common/pm2 (한국어)
description: "Node.js를 위한 프로세스 관리자."
content_hash: 334e59df21e7236506f7f6b7d2a74ce2860a471d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pm2.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pm2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pm2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pm2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pm2

Node.js를 위한 프로세스 관리자.
로그 관리, 모니터링 및 프로세스 구성을 위해 사용됩니다.
더 많은 정보: <https://pm2.keymetrics.io>.

- 나중에 사용할 수 있는 이름으로 프로세스를 시작:

`pm2 start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 프로세스 목록 나열:

`pm2 list`

- 모든 프로세스 모니터링:

`pm2 monit`

- 프로세스 중지:

`pm2 stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 프로세스 재시작:

`pm2 restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 나중에 복원할 수 있도록 모든 프로세스 덤프:

`pm2 save`

- 이전에 덤프한 프로세스 복원:

`pm2 resurrect`
