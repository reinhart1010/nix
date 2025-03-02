---
layout: page
title: linux/makepkg (中文)
description: "创建 `pacman` 可用的软件包。"
content_hash: b558695b57364982c3fa5c99a91a8996cbe154f6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/makepkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/makepkg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/makepkg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/makepkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/makepkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# makepkg

创建 `pacman` 可用的软件包。
默认使用当前工作目录中的 `PKGBUILD` 文件。
更多信息：<https://manned.org/makepkg.8>.

- 构建软件包：

`makepkg`

- 构建软件包并使用 `pacman` 安装缺失的依赖关系：

`makepkg --syncdeps`

- 构建软件包、安装缺失的依赖后将其安装到系统：

`makepkg --syncdeps --install`

- 构建软件包但不验证源文件的检验值：

`makepkg --skipchecksums`

- 编译后清理工作文件：

`makepkg --clean`

- 下载源文件（如果不存在）并进行完整性检查：

`makepkg --verifysource`

- 生成 `SRCINFO` 并写入到 `.SRCINFO` 文件：

`makepkg --printsrcinfo > .SRCINFO`
