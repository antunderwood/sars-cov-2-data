library(tidyverse)
library(googlesheets4)
library(magrittr)

colours <- googlesheets4::read_sheet("https://docs.google.com/spreadsheets/d/1adAawqzLYewFya7SsfKmaopSix-DbGE05RkyVe1C1Gw", sheet = "Lineage") %>% 
  select(key,colour) %>% 
  rename(lineage = key)

metadata <- read_csv("/Volumes/GoogleDrive/My Drive/documents/Manuscripts/phylocanvas/cog_metadata.csv")
metadata_with_colours <- metadata %>% left_join(colours, by = c("lineage")) %>% 
  select(-lineage)
write_csv(metadata_with_colours, "/Volumes/GoogleDrive/My Drive/documents/Manuscripts/phylocanvas/cog_metadata_with_colours.csv")
