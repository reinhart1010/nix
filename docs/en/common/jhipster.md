---
layout: page
title: common/jhipster (English)
description: "Web application generator using either monolithic or microservices architecture."
content_hash: e535c576d50ec41af93c2d60b337bd91d3ab36a9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# jhipster

Web application generator using either monolithic or microservices architecture.
More information: <https://www.jhipster.tech/>.

- Generate a simple full-stack project (monolithic or microservices):

`jhipster`

- Generate a simple frontend project:

`jhipster --skip-server`

- Generate a simple backend project:

`jhipster --skip-client`

- Apply latest JHipster updates to the project:

`jhipster upgrade`

- Add a new entity to a generated project:

`jhipster entity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entity_name</span>

- Import a JDL file to configure your application (see: <https://start.jhipster.tech/jdl-studio/>):

`jhipster import-jdl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first_file.jh second_file.jh ... n_file.jh</span>

- Generate a CI/CD pipeline for your application:

`jhipster ci-cd`

- Generate a Kubernetes configuration for your application:

`jhipster kubernetes`
