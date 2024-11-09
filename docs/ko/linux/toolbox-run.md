---
layout: page
title: linux/toolbox-run (한국어)
description: "기존 `toolbox` 컨테이너에서 명령을 실행합니다."
content_hash: 7d1c12de09154245d72f8d442506330dc2bff02f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/toolbox-run.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/toolbox-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/toolbox-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># toolbox run

기존 `toolbox` 컨테이너에서 명령을 실행합니다.
같이 보기: `toolbox enter`.
더 많은 정보: <https://manned.org/toolbox-run>.

- 특정 `toolbox` 컨테이너 내에서 명령 실행:

`toolbox run --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 특정 배포판 릴리스의 `toolbox` 컨테이너 내에서 명령 실행:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포판</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">릴리스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- Fedora 39의 기본 이미지로 `toolbox` 컨테이너 내에서 `emacs` 실행:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>
