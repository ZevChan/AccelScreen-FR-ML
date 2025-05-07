# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:03:22 2024

@author: WINDOWS
"""

# 定义文件路径  
file1_path = "20240612_SMILES_COMBINE_48w-valid_smiles.txt"  
file2_path = "20240612_SMILES_COMBINE_48w-valid_smiles_RandomizeMol_2x.txt"  
common_smiles_path = "common_smiles.txt"  
unique_to_file1_path = "unique_to_file1.txt"  
unique_to_file2_path = "unique_to_file2.txt"  
  
# 使用集合来存储SMILES  
set_smiles1 = set()  
set_smiles2 = set()  
  
# 读取文件并填充集合  
with open(file1_path, "r") as file1:  
    set_smiles1.update(file1.read().splitlines())  
  
with open(file2_path, "r") as file2:  
    set_smiles2.update(file2.read().splitlines())  
  
# 找出相同的SMILES  
common_smiles = set_smiles1.intersection(set_smiles2)  
  
# 找出只存在于file1中的SMILES  
unique_to_file1 = set_smiles1 - common_smiles  
  
# 找出只存在于file2中的SMILES  
unique_to_file2 = set_smiles2 - common_smiles  
  
# 将结果写入文件  
with open(common_smiles_path, "w") as common_file:  
    for smile in common_smiles:  
        common_file.write(smile + "\n")  
  
with open(unique_to_file1_path, "w") as unique_file1:  
    for smile in unique_to_file1:  
        unique_file1.write(smile + "\n")  
  
with open(unique_to_file2_path, "w") as unique_file2:  
    for smile in unique_to_file2:  
        unique_file2.write(smile + "\n")  
  
# 文件写入完成