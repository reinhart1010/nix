---
layout: page
title: linux/togglesebool (한국어)
description: "SELinux 부울의 현재 (비영구적) 값을 변경."
content_hash: b67a27016d7fdebe54eb4d463a79d4379ce61661
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/togglesebool.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/togglesebool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/togglesebool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># togglesebool

SELinux 부울의 현재 (비영구적) 값을 변경.
참고: 이 도구는 `setsebool`로 대체되어 더 이상 사용되지 않거나 제거되었습니다.
더 많은 정보: <https://manned.org/togglesebool>.

- 지정된 부울의 현재 (비영구적) 값을 변경:

`sudo togglesebool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virt_use_samba virt_use_usb ...</span>
