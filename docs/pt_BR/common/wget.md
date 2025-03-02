---
layout: page
title: common/wget (português (Brasil))
description: "Baixar arquivos da Internet."
content_hash: 34128f39171da0f8bd3353e1713353963e3e1ee1
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/common/wget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/wget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/wget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wget

Baixar arquivos da Internet.
Suporta HTTP, HTTPS, e FTP.
Mais informações: <https://www.gnu.org/software/wget>.

- Baixa o conteúdo de uma URL para o arquivo (nomeado como "foo" neste caso):

`wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- Baixa o conteúdo de uma URL para o arquivo (nomeado como "bar" neste caso):

`wget --output-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- Baixa uma única página web e todo os seus recursos com intervalos de 3 segundos entre requisições (scripts, stylesheets, imagens, etc.):

`wget --page-requisites --convert-links --wait=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/algumapagina.html</span>

- Baixa todos os arquivos listados dentro de um diretório e seus sub-diretórios (não baixa elementos de página incorporados):

`wget --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/algumcaminho/</span>

- Limita a velocidade de download e o número de novas tentativas de conexão:

`wget --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/algumcaminho/</span>

- Baixa um arquivo de um servidor HTTP usando Autenticação Básica (também funciona para FTP):

`wget --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomeusuario</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Continua um download incompleto:

`wget --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Baixa todas as URLs armazenadas em um arquivo de texto para um diretório específico:

`wget --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>
