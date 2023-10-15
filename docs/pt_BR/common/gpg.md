---
layout: page
title: common/gpg (português (Brasil))
description: "GNU Privacy Guard."
content_hash: 8cfeab9f9c529a09e480cf470dad7e3311ecd4a7
last_modified_at: 2023-10-15
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
Veja `gpg2` para o GNU Privacy Guard 2. A maioria dos sistemas operacionais criam link simbólico entre `gpg` e `gpg2`.
Mais informações: <https://gnupg.org>.

- Cria uma chave GPG pública e privada interativamente:

`gpg --full-generate-key`

- Assina doc.txt sem criptografia (cria um arquivo de saída `doc.txt.asc`):

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Criptografa e assina `doc.txt` para alice@example.com e bob@example.com (cria um arquivo de saída `doc.txt.gpg`):

`gpg --encrypt --sign --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bob@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Criptografa `doc.txt` apenas com uma senha simétrica (cria um arquivo de saída `doc.txt.gpg`):

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- Descriptografa `doc.txt.gpg` (envia saída para `stdout`):

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- Importa uma chave pública:

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- Exporta a chave pública da alice@example.com (envia saída para `stdout`):

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- Exporta chave privada da alice@example.com (envia saída para `stdout`):

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
