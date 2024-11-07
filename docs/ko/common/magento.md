---
layout: page
title: common/magento (한국어)
description: "Magento PHP 프레임워크 관리."
content_hash: 37d01937e5bda8be6313b80baf2054aed8eee02b
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/magento.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/magento.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># magento

Magento PHP 프레임워크 관리.
더 많은 정보: <https://experienceleague.adobe.com/en/docs/commerce-operations/tools/cli-reference/commerce-on-premises>.

- 하나 이상의 모듈 활성화:

`magento module:enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈1 모듈2 ...</span>

- 하나 이상의 모듈 비활성화:

`magento module:disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈1 모듈2 ...</span>

- 모듈 활성화 후 데이터베이스 업데이트:

`magento setup:upgrade`

- 코드 및 의존성 주입 구성 업데이트:

`magento setup:di:compile`

- 정적 에셋 배포:

`magento setup:static-content:deploy`

- 유지보수 모드 활성화:

`magento maintenance:enable`

- 유지보수 모드 비활성화:

`magento maintenance:disable`

- 사용 가능한 모든 명령 나열:

`magento list`
