---
layout: page
title: common/jf (中文)
description: "与 JFrog 产品进行交互，比如 Artifactory、Xray、Distribution、Pipelines 和 Mission Control。"
content_hash: 18302ce113982af936eb20dbb15afa9c1b6cb0a6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jf.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/jf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/jf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jf

与 JFrog 产品进行交互，比如 Artifactory、Xray、Distribution、Pipelines 和 Mission Control。
更多信息：<https://jfrog.com/help/r/jfrog-cli/usage>.

- 添加一个新配置：

`jf config add`

- 显示当前配置：

`jf config show`

- 在给定的仓库和目录中搜索制品：

`jf rt search --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库名称</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径</span>`/`
