---
layout: page
title: common/mvn (português (Brasil))
description: "Ferramenta para a criação e gerenciamento de projetos Java."
content_hash: aaa215dfc8bb3fcf2405859584f3619c842e20b9
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/mvn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mvn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mvn

Ferramenta para a criação e gerenciamento de projetos Java.
Mais informações: <https://maven.apache.org>.

- Compila um projeto:

`mvn compile`

- Cria um artefato de distribuição utilizando o formato espeficado no `pom.xml`, por exemplo o formato `jar`:

`mvn package`

- Cria um artefato de distribuição sem executar testes unitários:

`mvn package -DskipTests`

- Instala um artefato gerado em um repositório local:

`mvn install`

- Apaga artefatos gerados no diretório `target`:

`mvn clean`

- Executa as fases `clean` e `package` em um projeto:

`mvn clean package`

- Executa as fases `clean` e `package` em um projeto utilizando um perfil:

`mvn clean -P`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>` package`

- Executa uma classe que possua o método `main`:

`mvn exec:java -Dexec.mainClass="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome.do.pacote.classe</span>`" -Dexec.args="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>`"`
