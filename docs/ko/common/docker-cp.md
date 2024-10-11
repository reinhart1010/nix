---
layout: page
title: common/docker-cp (한국어)
description: "호스트와 컨테이너 파일 시스템 간에 파일이나 디렉토리를 복사."
content_hash: 0716650fe43a83d56750e8fa3b4d9f90088fe109
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-cp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-cp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker cp

호스트와 컨테이너 파일 시스템 간에 파일이나 디렉토리를 복사.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/cp/>.

- 호스트에서 컨테이너로 파일이나 디렉토리 복사:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트의/파일_또는_디렉토리_경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너의/파일_또는_디렉토리_경로</span>

- 컨테이너에서 호스트로 파일이나 디렉토리 복사:

`docker cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너의/파일_또는_디렉토리_경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트의/파일_또는_디렉토리_경로</span>

- 호스트에서 컨테이너로 심볼릭 링크를 따라 파일이나 디렉토리 복사 (심볼릭 링크가 아닌 링크된 파일을 직접 복사):

`docker cp --follow-link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트의/심볼릭_링크_경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너의/파일_또는_디렉토리_경로</span>
