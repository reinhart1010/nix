---
layout: page
title: common/beanstalkd (한국어)
description: "단순하고 일반적인 work-queue 서버."
content_hash: 8c074c90c3fa3352e6c8ce125eb2e1efe7102974
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/beanstalkd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/beanstalkd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# beanstalkd

단순하고 일반적인 work-queue 서버.
더 많은 정보: <https://beanstalkd.github.io/>.

- beanstalkd를 시작하고, 11300 포트로 듣기:

`beanstalkd`

- 사용자가 지정한 포트 및 주소에서 beanstalkd 듣기 시작:

`beanstalkd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>

- work queue를 디스크에 저장하고 유지:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/persistence_directory</span>

- 500밀리초마다 지속성있는 디렉토리에 동기화:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/persistence_directory</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
