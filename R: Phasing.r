#========================================================================
# Phasing haplótipos
#========================================================================
#
# (C) Copyright 2024, by GP-PGx-UFTM and Contributors.
#
# 
#-----------------
#  
#-----------------
#
# Original Author:  Isadora Helena Tassoni, Guilherme Belfort-Almeida, Caique Manochio
# Contributor(s):  
# Updated by (and date): Guilherme Belfort-Almeida (02/08/2024)
#
# Dependencies: R
#
# Command line:

library(haplo.stats)
library(dplyr)
library(tidyr)
library(stringr)
library(readxl)

Input <- read_xlsx(choose.files(), sheet = "startg")

SNPsseparadosNAT <- Input %>%
  separate_wider_delim(rs4244285star2, "/", names = c("rs4244285star2_1", "rs4244285star2_2")) %>%
  separate_wider_delim(rs4986893star3, "/", names = c("rs4986893star3_1", "rs4986893star3_2")) %>%
  separate_wider_delim(rs12248560star17, "/", names = c("rs12248560star17_1", "rs12248560star17_2")) %>%
  separate_wider_delim(rs2860840, "/", names = c("rs2860840_1", "rs2860840_2")) %>%
  separate_wider_delim(rs11188059, "/", names = c("rs11188059_1", "rs11188059_2"))

SNPsNATSemID <- SNPsseparadosNAT
SNPsNATSemID$ID Pacientes <- NULL
SNPsNATSemID$PRU <- NULL

resulthaplos <- haplo.em(as.matrix(SNPsNATSemID), locus.label = c('rs4244285star2','rs4986893star3',
                                                                     'rs12248560star17', 'rs2860840', 'rs11188059'), miss.val=NA)
resulthaplos[["haplotype"]]

library(openxlsx)

resultadohaplo <- summary(resulthaploNAT)

write.xlsx(resultadohaplo, 'HaploStarTG.xlsx')
