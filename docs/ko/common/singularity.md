---
layout: page
title: common/singularity (한국어)
description: "Singularity 컨테이너 및 이미지 관리."
content_hash: 07b04ca8ffecb373be9cdcf1d0fb324b9ba82431
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/singularity.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/singularity.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># singularity

Singularity 컨테이너 및 이미지 관리.
더 많은 정보: <https://singularity-docs.readthedocs.io/en/latest/#commands>.

- Sylabs Cloud에서 원격 이미지 다운로드:

`singularity pull --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">library://godlovedc/funny/lolcow:latest</span>

- 최신 Singularity 이미지 형식으로 원격 이미지 재구축:

`singularity build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker://godlovedc/lolcow</span>

- 이미지에서 컨테이너를 시작하고 내부에서 셸 실행:

`singularity shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.sif</span>

- 이미지에서 컨테이너를 시작하고 명령 실행:

`singularity exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 이미지에서 컨테이너를 시작하고 내부 runscript 실행:

`singularity run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.sif</span>

- 레시피 파일에서 Singularity 이미지 생성:

`sudo singularity build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.sif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레시피</span>
