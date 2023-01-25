# Brief description of the datasets I will use for this project

1. TCGA data
WE will retrieve TCGA gene expression data from 

https://portal.gdc.cancer.gov/repository?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.case_id%22%2C%22value%22%3A%5B%22dcd5860c-7e3a-44f3-a732-fe92fe3fe300%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.data_category%22%2C%22value%22%3A%5B%22Transcriptome%20Profiling%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files

Data might be for isoforms not genes so may need to summarize

2. A data file with gene expression profile
It will contain a matrix with gene symbol or id and gene expression on each row

Ideally it will be Gene NCBI Entrez id for the gene ID and TPM values for the gene expression   

This file will be provided by the user, I will have data for testing
