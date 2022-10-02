---
layout: page
title: common/yarn (Deutsch)
description: "JavaScript und Node.js Paket-Manager Alternative."
content_hash: 9db3eff2d4d7c9ef571fd611df23053bfd6a1489
related_topics:
  - title: English version
    url: /en/common/yarn.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/yarn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yarn.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># yarn

JavaScript und Node.js Paket-Manager Alternative.
Weitere Informationen: <https://yarnpkg.com>.

- Installiere ein Modul global:

`yarn global add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Installiere alle in der `package.json` Datei genannten Dependencies (`install` ist optional):

`yarn install`

- Installiere ein Modul und füge es als Dependency der `package.json` Datei hinzu (`--dev` um es als Dev-Dependency zu installieren):

`yarn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Deinstalliere ein Modul und entferne es von der `package.json` Datei:

`yarn remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Erstelle interaktiv eine `package.json` Datei:

`yarn init`

- Indentifiziere ob ein Modul eine Dependency ist und liste andere Module, die von diesem abhängen:

`yarn why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>
