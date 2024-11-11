---
layout: page
title: linux/gedit (한국어)
description: "GNOME 데스크톱 프로젝트의 텍스트 편집기."
content_hash: 5552d6d14a936e2f5a109f44113fedf3f2f1379b
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/gedit.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/gedit.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/gedit.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/gedit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/gedit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gedit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gedit

GNOME 데스크톱 프로젝트의 텍스트 편집기.
더 많은 정보: <https://help.gnome.org/users/gedit/stable/>.

- 텍스트 파일 열기:

`gedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 여러 텍스트 파일 열기:

`gedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 파일2 ...</span>

- 특정 인코딩으로 텍스트 파일 열기:

`gedit --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지원되는 인코딩 목록 표시:

`gedit --list-encodings`
