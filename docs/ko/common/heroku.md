---
layout: page
title: common/heroku (한국어)
description: "Heroku 애플리케이션 생성 및 관리."
content_hash: 95b00577d071741f461224700398aabc9f0b6cf2
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/heroku.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/heroku.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/heroku.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># heroku

Heroku 애플리케이션 생성 및 관리.
더 많은 정보: <https://www.heroku.com/>.

- Heroku 계정에 로그인:

`heroku login`

- Heroku 애플리케이션 생성:

`heroku create`

- 애플리케이션 로그 표시:

`heroku logs --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- dyno (Heroku 가상 머신) 내에서 일회성 프로세스를 실행:

`heroku run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>` --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 애플리케이션의 dynos (Heroku 가상 머신) 나열:

`heroku ps --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- 애플리케이션 영구적으로 삭제:

`heroku destroy --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>
