---
layout: page
title: common/zeek (中文)
description: "被动网络流量分析器。"
content_hash: 42051ac42cf713dee26517f2d51a677afb50e0ce
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zeek.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zeek.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zeek.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zeek

被动网络流量分析器。
所有输出和日志文件将保存到当前工作目录。
更多信息：<https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- 分析来自网络接口的实时流量：

`sudo zeek --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口</span>

- 分析来自网络接口的实时流量并加载自定义脚本：

`sudo zeek --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">脚本1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">脚本2</span>

- 分析来自网络接口的实时流量，不加载任何脚本：

`sudo zeek --bare-mode --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口</span>

- 分析来自网络接口的实时流量，应用 `tcpdump` 过滤器：

`sudo zeek --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/过滤器</span>` --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口</span>

- 使用看门狗计时器分析来自网络接口的实时流量：

`sudo zeek --watchdog --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接口</span>

- 分析来自 PCAP 文件的流量：

`zeek --readfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.trace</span>
