---
layout: page
title: linux/certbot (한국어)
description: "TLS 인증서를 자동으로 획득하고 갱신하기 위한 Let's Encrypt 에이전트."
content_hash: 371412fe51b6feccac2f790734bf876b08d5ecc6
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/certbot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/certbot.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/certbot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/certbot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/certbot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># certbot

TLS 인증서를 자동으로 획득하고 갱신하기 위한 Let's Encrypt 에이전트.
`letsencrypt`의 후속 도구.
더 많은 정보: <https://certbot.eff.org/docs/using.html>.

- 웹루트 인증을 통해 새 인증서를 획득하지만 자동으로 설치하지 않기:

`sudo certbot certonly --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/웹루트</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인.example.com</span>

- nginx 인증을 통해 새 인증서를 획득하고 자동으로 설치하기:

`sudo certbot --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인.example.com</span>

- apache 인증을 통해 새 인증서를 획득하고 자동으로 설치하기:

`sudo certbot --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인.example.com</span>

- 30일 이내에 만료되는 모든 Let's Encrypt 인증서 갱신하기 (사용하고 있는 서버를 잊지 말고 재시작하기):

`sudo certbot renew`

- 새 인증서 획득을 시뮬레이션하지만 실제로 디스크에 인증서를 저장하지 않기:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/웹루트</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인.example.com</span>` --dry-run`

- 신뢰할 수 없는 테스트 인증서 획득하기:

`sudo certbot --webroot --webroot-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/웹루트</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인.example.com</span>` --test-cert`
