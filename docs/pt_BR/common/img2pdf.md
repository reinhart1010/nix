---
layout: page
title: common/img2pdf (português (Brasil))
description: "Ferramenta de conversão sem perdas de imagens para PDF."
content_hash: 7a81ac2190644ea2977ccafb691e46c875a1de85
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/img2pdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# img2pdf

Ferramenta de conversão sem perdas de imagens para PDF.
Mais informações: <https://gitlab.mister-muffin.de/josch/img2pdf>.

- Converte múltiplas imagens para um único PDF, cada imagem sendo uma página:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/da/imagem1.ext caminho/da/imagem2.ext ...</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.pdf</span>

- Converte para PDF apenas o primeiro quadro de uma imagem com múltiplos quadros:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.gif</span>` --first-frame-only --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.pdf</span>

- Auto-orientar a imagem, usando uma página A4 em modo paisagem e uma borda de 2cm horizontalmente e 5.1cm verticalmente:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.ext</span>` --auto-orient --pagesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A4^T</span>` --border `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2cm</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5.1cm</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.pdf</span>

- Encolhe apenas imagens maiores para um retângulo de 10cm por 15cm dentro de uma página de 30x20cm:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.tiff</span>` --pagesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30cm</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20cm</span>` --imgsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10cm</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15cm</span>` --fit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shrink</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.pdf</span>

- Converte uma imagem para PDF e especifica os metadados do arquivo resultante:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.png</span>` --title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título</span>` --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autor</span>` --creationdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1970-01-31</span>` --keywords `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra_chave1 palavra_chave2</span>` --subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assunto</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo.pdf</span>
