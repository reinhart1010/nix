---
layout: page
title: linux/semanage-permissive (한국어)
description: "지속적인 SELinux 허용 도메인 관리."
content_hash: af12870395940e639ede0e8fc5c4845538aa520c
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/semanage-permissive.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/semanage-permissive.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/semanage-permissive.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># semanage permissive

지속적인 SELinux 허용 도메인 관리.
이로 인해 프로세스가 비구속 상태가 될 수 있으므로, 장기적으로 사용할 경우 SELinux를 올바르게 구성하는 것이 좋습니다.
같이 보기: `semanage`, `getenforce`, `setenforce`.
더 많은 정보: <https://manned.org/semanage-permissive>.

- 허용 모드에 있는 모든 프로세스 유형(도메인) 나열:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- 도메인에 대한 허용 모드를 설정하거나 해제:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>
