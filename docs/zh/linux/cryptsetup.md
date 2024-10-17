---
layout: page
title: linux/cryptsetup (中文)
description: "管理普通 dm-crypt 和 LUKS（Linux 统一密钥设置）加密卷。"
content_hash: 6a52dfb5b70805cf8e0ab6ab98efc60d60383170
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/linux/cryptsetup.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cryptsetup

管理普通 dm-crypt 和 LUKS（Linux 统一密钥设置）加密卷。
更多信息：<https://gitlab.com/cryptsetup/cryptsetup/>.

- 初始化 LUKS 卷（覆盖分区上的所有数据）：

`cryptsetup luksFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- 打开 LUKS 卷并在 `/dev/mapper/目标` 创建解密映射：

`cryptsetup luksOpen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 删除已存在的映射：

`cryptsetup luksClose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标</span>

- 更改 LUKS 卷的口令：

`cryptsetup luksChangeKey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
