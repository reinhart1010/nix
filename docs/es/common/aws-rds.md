---
layout: page
title: common/aws-rds (español)
description: "CLI para AWS Relational Database Service."
content_hash: cb42272a23d0db148c51546b6f3f7187a6fc3853
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/aws-rds.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-rds.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws rds

CLI para AWS Relational Database Service.
Crea y administra bases de datos relacionales.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Muestra ayuda para subcomando RDS específicos:

`aws rds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`

- Detiene instancia:

`aws rds stop-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_instancia</span>

- Inicia instancia:

`aws rds start-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_instancia</span>

- Modifica una instancia RDS:

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_instancia</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parametros</span>` --apply-immediately`

- Aplica actualizaciones a una instancia RDS:

`aws rds apply-pending-maintenance-action --resource-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_arn</span>` --apply-action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system-update</span>` --opt-in-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immediate</span>

- Modifica un identificador de instancia:

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antiguo_identificador_instancia</span>` --new-db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_identificador_instancia</span>

- Reinicia una instancia:

`aws rds reboot-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_instancia</span>

- Elimina una instancia:

`aws rds delete-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_instancia</span>` --final-db-snapshot-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_snapshot</span>` --delete-automated-backups`
