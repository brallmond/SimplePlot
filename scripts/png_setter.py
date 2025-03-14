import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('input_dir', help='input_directory')
#args = parser.parse_args()

#input_dir = args.input_dir #"FS_plots/plots_ditau_Inclusive_from_14-03_at_0901"
# AR, DRar, #AR_aiso, DRar_aiso
# SR, DRsr, #SR_aiso, DRsr_aiso
input_dirs = [
"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1537", #AR
"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1616", #DRar
"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1623", #SR
"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1618", #DRsr
]
#input_dirs = [
#"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1639", #AR_aiso
#"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1642", #DRar_aiso
#"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1645", #SR_aiso
#"FS_plots/plots_ditau_NoneTauPtCategory_0j_from_04-02_at_1647", #DRsr_aiso
#]

# for ditau
files = ["FS_t1_pt.png", "FS_t1_eta.png", "FS_t1_phi.png", "HTT_m_vis-KSUbinning.png",
         "FS_t2_pt.png", "FS_t2_eta.png", "FS_t2_phi.png", "PuppiMET_pt.png"]

filetype = "FS_t2_phi" 
  
images = []
for input_dir in input_dirs:
  ls = os.listdir(input_dir)
  get_file = [filename for filename in ls if filetype in filename]
  print(get_file)
  special_idx = {"FS_t1_DM" : 1, "FS_t2_DM" : 2, "FS_t1_mass" : 2, "FS_t2_mass" : 1}
  get_file = get_file[0] if len(get_file) == 1 else get_file[special_idx[filetype]]
  file_string = input_dir + "/" + get_file
  images.append(np.array(Image.open(file_string)))

fig = plt.figure(figsize=(64,56), layout="tight")

ax = fig.add_subplot(2, 2, 1)
plt.imshow(images[0]); plt.axis('off') #AR
ax = fig.add_subplot(2, 2, 2)
plt.imshow(images[1]); plt.axis('off') # DRar
ax = fig.add_subplot(2, 2, 3)
plt.imshow(images[2]); plt.axis('off') # SR
ax = fig.add_subplot(2, 2, 4)
plt.imshow(images[3]); plt.axis('off') # DRsr

#for i in range(0,len(images)):
#  if i <= 3:
#    ax = fig.add_subplot(1, 2, i+1)
#  else:
#    ax = fig.add_subplot(2, 2, i+1)
#  plt.imshow(images[i])
#  plt.axis('off')

filename = "FF_collected_plots"
print(f"saving as {filename}.png")
plt.savefig(filename+".png", bbox_inches="tight")
plt.close()








