---
layout: page
title: linux/slurmrestd (한국어)
description: "REST API를 통해 Slurm에 인터페이스를 제공하는 도구입니다. *Inetd 모드* 및 *Listen 모드*에서 사용할 수 있습니다."
content_hash: 0feaab059d3fa285f1403e4a2288b91922736f2b
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/slurmrestd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/slurmrestd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># slurmrestd

REST API를 통해 Slurm에 인터페이스를 제공하는 도구입니다. *Inetd 모드* 및 *Listen 모드*에서 사용할 수 있습니다.
더 많은 정보: <https://slurm.schedmd.com/slurmrestd.html>.

- 클라이언트 요청을 처리하기 전에 그룹 ID를 변경하고 보조 그룹을 제거:

`slurmrestd --g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[호스트]:포트 | unix:/경로/대상/소켓</span>

- 로드할 인증 플러그인의 쉼표로 구분된 목록:

`slurmrestd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인증_플러그인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[호스트]:포트 | unix:/경로/대상/소켓</span>

- 지정된 파일에서 Slurm 설정 읽기:

`slurmrestd -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 클라이언트 요청을 처리하기 전에 사용자 ID 변경:

`slurmrestd -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_ID</span>

- 도움말 표시:

`slurmrestd -h`

- 버전 표시:

`slurmrestd -V`
