from ete3 import Tree
import pandas as pd


# make new dict with names as keys and concatenated name/lineages as values
metadata = pd.read_csv("cog_metadata.csv")
metadata['name_and_lineage'] = metadata['sequence_name'] + "#" + metadata['lineage']
metadata_dict = dict(zip(metadata['sequence_name'], metadata['name_and_lineage']))

# Make new tree file with revised concatenated name/lineages labels
tree = Tree("cog_global_tree.nwk")
for leaf in tree.iter_leaves():
  leaf.name = metadata_dict[leaf.name]

tree.write(format=1, outfile="cog_global_tree.plus_lineages.nwk")

gsheet = pd.read_excel(
    "https://docs.google.com/spreadsheets/d/1adAawqzLYewFya7SsfKmaopSix-DbGE05RkyVe1C1Gw/export?format=xlsx",
    sheet_name="Lineage",
    engine="openpyxl")
    
metadata_with_colours = metadata.merge(gsheet, left_on = 'lineage', right_on = 'key')
  
 
