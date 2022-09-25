---
layout: page
title: common/acme.sh (中文)
description: "实现了 ACME 客户端协议的 shell 脚本，是 certbot 的替代品。"
content_hash: 863659724324fce0344728ef77a3ba68b7651d00
related_topics:
  - title: English version
    url: /en/common/acme.sh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acme.sh.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># acme.sh

实现了 ACME 客户端协议的 shell 脚本，是 certbot 的替代品。
另见 `acme.sh dns`。
更多信息：<https://github.com/acmesh-official/acme.sh>.

- 使用网站根目录模式签发证书：

`acme.sh --issue --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --webroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/网站根目录</span>

- 使用独立模式和 80 端口为多个域名签发证书：

`acme.sh --issue --standalone --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 使用独立 TLS 模式和 443 端口签发证书：

`acme.sh --issue --alpn --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 使用运行中的 Nginx 的配置来签发证书：

`acme.sh --issue --nginx --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 使用运行中的 Apache 的配置来签发证书：

`acme.sh --issue --apache --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 使用自动 DNS API 模式签发一个通配符（\*）证书：

`acme.sh --issue --dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_cf</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.example.com</span>

- 将证书文件安装到指定位置（对自动更新证书很有用）：

`acme.sh --install-cert -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/example.com.key</span>` --fullchain-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/example.com.cer</span>` --reloadcmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"systemctl force-reload nginx"</span>
