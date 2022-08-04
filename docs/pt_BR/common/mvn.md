---
layout: page
title: common/mvn (português (Brasil))
description: "Ferramenta para a criação e gerenciamento de projetos Java."
content_hash: baf8cf58057bd9c61585c3e05b0da2e2e6048aad
related_topics:
  - title: English version
    url: /en/common/mvn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mvn.html
    icon: bi bi-globe
---
# mvn

Ferramenta para a criação e gerenciamento de projetos Java.
Mais informações: <https://maven.apache.org>.

- Compilar um projeto:

`mvn compile`

- Criar um artefato de distribuição utilizando o formato espeficado no `pom.xml`, por exemplo o formato `jar`:

`mvn package`

- Criar um artefato de distribuição sem executar testes unitários:

`mvn package -DskipTests`

- Instalar um artefato gerado em um repositório local:

`mvn install`

- Apagar artefatos gerados no diretório `target`:

`mvn clean`

- Executar as fases `clean` e `package` em um projeto:

`mvn clean package`

- Executar as fases `clean` e `package` em um projeto utilizando um perfil:

`mvn clean -P`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perfil</span>` package`

- Executar uma classe que possua o método `main`:

`mvn exec:java -Dexec.mainClass="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome.do.pacote.classe</span>`" -Dexec.args="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2</span>`"`
