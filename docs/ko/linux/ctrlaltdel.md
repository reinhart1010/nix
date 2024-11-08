---
layout: page
title: linux/ctrlaltdel (한국어)
description: "CTRL+ALT+DEL 키 조합을 눌렀을 때의 동작을 제어하는 도구."
content_hash: 7c61c80bf1eefb2c7893d0308f3c2235df5eeb74
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/ctrlaltdel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ctrlaltdel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ctrlaltdel

CTRL+ALT+DEL 키 조합을 눌렀을 때의 동작을 제어하는 도구.
더 많은 정보: <https://manned.org/ctrlaltdel>.

- 현재 설정 확인:

`ctrlaltdel`

- CTRL+ALT+DEL을 즉시 재부팅하도록 설정 (준비 없이):

`sudo ctrlaltdel hard`

- CTRL+ALT+DEL을 "일반적으로" 재부팅하도록 설정, 프로세스 종료 기회를 제공 (PID1에 SIGINT 전송):

`sudo ctrlaltdel soft`
