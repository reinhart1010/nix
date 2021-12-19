---
layout: page
title: windows/repair-bde (中文)
description: "尝试修复或解密损坏的 BitLocker 加密卷。"
content_hash: 4b9e453896b8cb0548243b912f68ddaca1a12158
related_topics:
  - title: English version
    url: /en/windows/repair-bde.html
    icon: bi bi-globe
---
# repair-bde

尝试修复或解密损坏的 BitLocker 加密卷。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- 尝试修复一个指定的卷：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>

- 尝试修复指定的卷并输出到另一个卷：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D:</span>

- 尝试使用提供的恢复密钥文件修复指定的卷：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -RecoveryKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bek 文件的路径</span>

- 尝试使用提供的数字恢复密码修复指定的卷：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -RecoveryPassword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 尝试使用提供的密码修复指定的卷：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -Password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 尝试使用提供的密钥包修复指定的卷：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -KeyPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

- 将日志输出到指定的文件：

`repair-bde `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -LogFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件的路径</span>

- 显示所有可用的选项：

`repair-bde /?`
