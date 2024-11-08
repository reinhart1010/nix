---
layout: page
title: common/puppet-apply (한국어)
description: "Puppet 매니페스트를 로컬에서 적용."
content_hash: 450126f03e65eb837f9110ca9c60890779d4c24e
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/puppet-apply.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/puppet-apply.html
    icon: bi bi-globe
tldri18n_status: 2
---
# puppet apply

Puppet 매니페스트를 로컬에서 적용.
더 많은 정보: <https://puppet.com/docs/puppet/7/man/apply.html>.

- 매니페스트 적용:

`puppet apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>

- Puppet 코드 실행:

`puppet apply --execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>

- 특정 모듈 및 Hiera 구성 파일 사용:

`puppet apply --modulepath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --hiera_config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트</span>
