---
layout: page
title: linux/blastp (한국어)
description: "단백질-단백질 BLAST."
content_hash: 019c79bb02669f10667e1520209dcae88bed5938
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/blastp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blastp

단백질-단백질 BLAST.
더 많은 정보: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastp_application_options/>.

- e-value 임계값이 1e-9인 경우, 쌍별 출력 형식으로 두 개 이상의 서열을 blastp로 정렬하고 화면에 출력:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상.fa</span>` -evalue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1e-9</span>

- blastp-fast를 사용하여 두 개 이상의 서열 정렬:

`blastp -task blastp-fast -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상.fa</span>

- 사용자 정의 테이블 형식으로 두 개 이상의 서열 정렬하고 파일에 출력:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리.fa</span>` -subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상.fa</span>` -outfmt '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident</span>`' -out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.tsv</span>

- 단백질 쿼리를 사용하여 단백질 데이터베이스 검색, BLAST 검색에 사용할 16개의 스레드, 최대 10개의 정렬된 서열 유지:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blast_데이터베이스_이름</span>` -num_threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` -max_target_seqs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 원격 비중복 단백질 데이터베이스를 단백질 쿼리로 검색:

`blastp -query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리.fa</span>` -db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nr</span>` -remote`

- 도움말 표시 (`-help`로 자세한 도움말 확인 가능):

`blastp -h`
