from PIL import Image
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("final_state", help="TauTau, MuTau, ETau, EMu")
parser.add_argument("era", help="2022_preEE, 2022_postEE, 2023_preBPix, 2023_postBPix, 2022, 2023, All")
parser.add_argument("var", help="HpT, nJets, j1pT")
args = parser.parse_args()

final_state = args.final_state
era = args.era
var = args.var
if var == "nJets": var = "nJet"
FSshort = {
  "TauTau" : "ditau",
  "MuTau"  : "mutau",
  "ETau"   : "etau",
  "EMu"    : "emu",
}

combinedInfo = f"_{era}_{FSshort[final_state]}_{var}.png"
combinedInfoLog = f"_{era}_{FSshort[final_state]}_{var}_log.png"

input_dir = "plots/"
tauPts = ["lowTauPt", "midTauPt", "highTauPt"]
filenames = [input_dir+tauPt+combinedInfo for tauPt in tauPts]
filenamesLog = [input_dir+tauPt+combinedInfoLog for tauPt in tauPts]

def produce_combined_figure(filenames, input_dir, combinedInfo):
  fig = plt.figure(figsize=(64, 56), layout="tight")
  for i, file in enumerate(filenames):
    ax = fig.add_subplot(3, 1, i+1)
    plt.imshow(Image.open(file))
    plt.axis('off')
  print(f"saving as {input_dir}combined/combined{combinedInfo}")
  plt.savefig(f"{input_dir}combined/combined{combinedInfo}")

produce_combined_figure(filenames, input_dir, combinedInfo)
produce_combined_figure(filenamesLog, input_dir, combinedInfoLog)


