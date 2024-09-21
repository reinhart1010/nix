---
layout: page
title: common/aws-vault (한국어)
description: "개발 환경에서 AWS 자격 증명을 안전하게 저장하고 액세스하기 위한 저장소."
content_hash: c5f27eb1f0003ddc1bef89c5d630991e6d3ef3e0
last_modified_at: 2024-09-21
related_topics:
  - title: Deutsch version
    url: /de/common/aws-vault.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-vault.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-vault.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws-vault

개발 환경에서 AWS 자격 증명을 안전하게 저장하고 액세스하기 위한 저장소.
더 많은 정보: <https://github.com/99designs/aws-vault>.

- 보안 키 저장소에 자격 증명을 추가:

`aws-vault add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 환경에서 AWS 자격 증명을 사용하여 명령을 실행:

`aws-vault exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws s3 ls</span>

- 브라우저 창을 열고 AWS 콘솔에 로그인:

`aws-vault login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 자격 증명 및 세션과 함께 프로필을 나열:

`aws-vault list`

- AWS 자격 증명 교체:

`aws-vault rotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 보안 키 저장소에서 자격 증명을 제거:

`aws-vault remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>
