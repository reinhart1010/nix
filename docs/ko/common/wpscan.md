---
layout: page
title: common/wpscan (한국어)
description: "WordPress 취약점 스캐너."
content_hash: e065a168eb40e03cb21a465ab7970a057bcb9ca7
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wpscan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wpscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wpscan

WordPress 취약점 스캐너.
더 많은 정보: <https://github.com/wpscanteam/wpscan>.

- 취약점 데이터베이스 업데이트:

`wpscan --update`

- WordPress 웹사이트 스캔:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 무작위 사용자 에이전트와 수동 감지를 사용하여 WordPress 웹사이트 스캔:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --stealthy`

- 취약한 플러그인을 확인하고 `wp-content` 디렉터리 경로를 지정하여 WordPress 웹사이트 스캔:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --enumerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vp</span>` --wp-content-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격/경로/대상/워드프레스-내용</span>

- 프록시를 통해 WordPress 웹사이트 스캔:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol://ip:port</span>` --proxy-auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명:비밀번호</span>

- WordPress 웹사이트에서 사용자 식별자 열거 수행:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --enumerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">u</span>

- WordPress 웹사이트에 대한 비밀번호 추측 공격 실행:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --usernames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명|경로/대상/사용자 명.txt</span>` --passwords `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀번호.txt</span>` threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- WPVulnDB (<https://wpvulndb.com/>)에서 취약점 데이터를 수집하여 WordPress 웹사이트 스캔:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --api-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>
