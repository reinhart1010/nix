---
layout: page
title: common/jarsigner (中文)
description: "签名并验证 Java 存档（JAR）文件。"
content_hash: b84eb92197531866ed44a2cd05eef919a6f2aba2
related_topics:
  - title: English version
    url: /en/common/jarsigner.html
    icon: bi bi-globe
---
# jarsigner

签名并验证 Java 存档（JAR）文件。
更多信息：<https://docs.oracle.com/javase/9/tools/jarsigner.htm>.

- 签名一个 `JAR` 文件：

`jarsigner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keystore_alias</span>

- 使用特定算法对 `JAR` 文件进行签名：

`jarsigner -sigalg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorithm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keystore_alias</span>

- 验证 `JAR` 文件的签名：

`jarsigner -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>
