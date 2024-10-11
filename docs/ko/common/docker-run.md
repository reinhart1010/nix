---
layout: page
title: common/docker-run (한국어)
description: "새로운 Docker 컨테이너에서 명령 실행."
content_hash: 9e29afa9fb19d1440843965d463770bcf46004d4
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-run.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-run.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-run.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-run.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-run.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-run.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker run

새로운 Docker 컨테이너에서 명령 실행.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/run/>.

- 태그가 지정된 이미지에서 새 컨테이너로 명령 실행:

`docker run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 백그라운드에서 새 컨테이너로 명령 실행하고 ID 표시:

`docker run --detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 일회성 컨테이너에서 대화형 모드와 가상 TTY로 명령 실행:

`docker run --rm --interactive --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 전달된 환경 변수를 사용하여 새 컨테이너로 명령 실행:

`docker run --env '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`' --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 바인드 마운트된 볼륨을 사용하여 새 컨테이너로 명령 실행:

`docker run --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/호스트_경로</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/컨테이너_경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 게시된 포트를 사용하여 새 컨테이너로 명령 실행:

`docker run --publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_포트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 이미지의 엔트리포인트를 덮어쓰며 새 컨테이너로 명령 실행:

`docker run --entrypoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 네트워크에 연결하여 새 컨테이너로 명령 실행:

`docker run --network `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>
