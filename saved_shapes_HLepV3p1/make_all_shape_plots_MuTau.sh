#!/bin/sh

python3 shape_plotter.py "lowTauPt" "MuTau" "2022_preEE" "HpT";
python3 shape_plotter.py "midTauPt" "MuTau" "2022_preEE" "HpT";
python3 shape_plotter.py "highTauPt" "MuTau" "2022_preEE" "HpT";

python3 shape_plotter.py "lowTauPt" "MuTau" "2022_postEE" "HpT";
python3 shape_plotter.py "midTauPt" "MuTau" "2022_postEE" "HpT";
python3 shape_plotter.py "highTauPt" "MuTau" "2022_postEE" "HpT";

python3 shape_plotter.py "lowTauPt" "MuTau" "2023_preBPix" "HpT";
python3 shape_plotter.py "midTauPt" "MuTau" "2023_preBPix" "HpT";
python3 shape_plotter.py "highTauPt" "MuTau" "2023_preBPix" "HpT";

python3 shape_plotter.py "lowTauPt" "MuTau" "2023_postBPix" "HpT";
python3 shape_plotter.py "midTauPt" "MuTau" "2023_postBPix" "HpT";
python3 shape_plotter.py "highTauPt" "MuTau" "2023_postBPix" "HpT";
echo "HpT done";

python3 shape_plotter.py "lowTauPt" "MuTau" "2022_preEE" "j1pT";
python3 shape_plotter.py "midTauPt" "MuTau" "2022_preEE" "j1pT";
python3 shape_plotter.py "highTauPt" "MuTau" "2022_preEE" "j1pT";

python3 shape_plotter.py "lowTauPt" "MuTau" "2022_postEE" "j1pT";
python3 shape_plotter.py "midTauPt" "MuTau" "2022_postEE" "j1pT";
python3 shape_plotter.py "highTauPt" "MuTau" "2022_postEE" "j1pT";

python3 shape_plotter.py "lowTauPt" "MuTau" "2023_preBPix" "j1pT";
python3 shape_plotter.py "midTauPt" "MuTau" "2023_preBPix" "j1pT";
python3 shape_plotter.py "highTauPt" "MuTau" "2023_preBPix" "j1pT";

python3 shape_plotter.py "lowTauPt" "MuTau" "2023_postBPix" "j1pT";
python3 shape_plotter.py "midTauPt" "MuTau" "2023_postBPix" "j1pT";
python3 shape_plotter.py "highTauPt" "MuTau" "2023_postBPix" "j1pT";
echo "j1pT done";

python3 shape_plotter.py "lowTauPt" "MuTau" "2022_preEE" "nJets";
python3 shape_plotter.py "midTauPt" "MuTau" "2022_preEE" "nJets";
python3 shape_plotter.py "highTauPt" "MuTau" "2022_preEE" "nJets";

python3 shape_plotter.py "lowTauPt" "MuTau" "2022_postEE" "nJets";
python3 shape_plotter.py "midTauPt" "MuTau" "2022_postEE" "nJets";
python3 shape_plotter.py "highTauPt" "MuTau" "2022_postEE" "nJets";

python3 shape_plotter.py "lowTauPt" "MuTau" "2023_preBPix" "nJets";
python3 shape_plotter.py "midTauPt" "MuTau" "2023_preBPix" "nJets";
python3 shape_plotter.py "highTauPt" "MuTau" "2023_preBPix" "nJets";

python3 shape_plotter.py "lowTauPt" "MuTau" "2023_postBPix" "nJets";
python3 shape_plotter.py "midTauPt" "MuTau" "2023_postBPix" "nJets";
python3 shape_plotter.py "highTauPt" "MuTau" "2023_postBPix" "nJets";
echo "nJets done";
