---
layout: page
title: common/aws (italiano)
description: "Il tool da linea di comando ufficiale per Amazon Web Services."
content_hash: 1cea7ba57d04639f2c146fef378b1c0ff75e9171
last_modified_at: 2024-10-05
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/aws.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws

Il tool da linea di comando ufficiale per Amazon Web Services.
Alcuni comandi aggiuntivi, come `s3`, hanno la propria documentazione.
Maggiori informazioni: <https://aws.amazon.com/cli>.

- Lista tutti gli utenti IAM (Identity and Access Management):

`aws iam list-users`

- Lista tutte le instanze EC2 per una specifica regione:

`aws ec2 describe-instances --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Ricevi un messaggio da una specifica coda SQS:

`aws sqs receive-message --queue-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://queue.amazonaws.com/546123/Test</span>

- Pubblica un messaggio SNS su uno specifico argomento:

`aws sns publish --topic-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn:aws:sns:us-east-1:54633:Agomento</span>` --message "Message"`

- Mostra la pagina di aiuto per uno specifico comando AWS:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` help`
