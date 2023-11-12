---
layout: page
title: common/acme.sh-dns (中文)
description: "使用 DNS-01 挑战来签发 TLS 证书。"
content_hash: 28a40fbb07e93ddd2ef3dbcf11d311d999a17156
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acme.sh-dns.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acme.sh-dns.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acme.sh --dns

使用 DNS-01 挑战来签发 TLS 证书。
更多信息：<https://github.com/acmesh-official/acme.sh/wiki>.

- 使用自动 DNS API 模式签发证书：

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gnd_gd</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 使用自动 DNS API 模式签发通配符证书（用星号表示）：

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namesilo</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- 使用 DNS 别名模式签发证书：

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --challenge-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias-for-example-validation.com</span>

- 在添加 DNS 记录后，通过指定自定义的等待时间（秒），在禁用 Cloudflare / Google DNS 自动轮询的同时签发证书：

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_namecheap</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --dnssleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>

- 使用手动 DNS 模式签发证书：

`acme.sh --issue --dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --yes-I-know-dns-manual-mode-enough-go-ahead-please`
