---
layout: page
title: common/gpg (português (Brasil))
description: "GNU Privacy Guard."
content_hash: 263d14c43a2fb85d57ae5ecdce750d4dcb497b53
related_topics:
  - title: Deutsch version
    url: /de/common/gpg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gpg.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gpg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpg

GNU Privacy Guard.
Mais informações: <https://gnupg.org>.

- Assina doc.txt, sem criptografá-lo (cria um arquivo de saída doc.txt.asc):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Criptografa doc.txt para alice@example.com (cria um arquivo de saída `doc.txt.gpg`):

`gpg --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Criptografa doc.txt apenas com uma senha simétrica (cria um arquivo de sadída `doc.txt.gpg`):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Descriptografa doc.txt.gpg (envia saída para stdout):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- Importa uma chave pública:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- Exporta a chave pública da alice@example.com (envia saída para stdout):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- Exporta chave privada da alice@example.com (envia saída para stdout):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
