import rich
#import correctionlib
import correctionlib.schemav2 as cs

# binning is always
global_edges=[0, 10, 20, 30, 40, 60, 80, 120, 200, 350, 450, 600, 9999]

# this is sort of ridiculous, but it's easier to update this than to scroll 
# through and update all the indentations properly

# note preEE uses V5 samples while all other eras use V6
preEE_ggH_Inc   = [3.205, 1.510, 1.069, 0.905, 0.957, 1.188, 1.343, 1.399, 1.405, 1.396, 1.383, 1.368]
preEE_ggH_0j    = [3.178, 1.485, 1.025, 0.813, 0.650, 0.544, 0.666, 1.440, 1.407, 1.369, 1.000, 1.000]
preEE_ggH_GTE1j = [5.965, 2.944, 2.044, 1.658, 1.473, 1.394, 1.370, 1.398, 1.405, 1.396, 1.383, 1.368]
preEE_VBF_Inc   = [5.338, 2.547, 1.843, 1.573, 1.476, 1.422, 1.384, 1.359, 1.355, 1.359, 1.349, 1.373]
preEE_VBF_0j    = [5.310, 2.440, 1.679, 1.322, 1.161, 1.223, 1.387, 1.407, 1.411, 1.523, 1.565, 1.000]
preEE_VBF_GTE1j = [5.372, 2.641, 1.933, 1.644, 1.507, 1.429, 1.384, 1.359, 1.355, 1.358, 1.349, 1.373]

postEE_ggH_Inc   = [3.185, 1.518, 1.068, 0.914, 0.972, 1.177, 1.328, 1.387, 1.393, 1.396, 1.355, 1.357]
postEE_ggH_0j    = [3.158, 1.496, 1.026, 0.819, 0.659, 0.527, 0.607, 1.398, 1.516, 1.321, 1.000, 1.000]
postEE_ggH_GTE1j = [6.543, 2.974, 2.147, 1.726, 1.472, 1.366, 1.355, 1.387, 1.393, 1.396, 1.355, 1.357]
postEE_VBF_Inc   = [5.564, 2.597, 1.848, 1.626, 1.493, 1.428, 1.384, 1.346, 1.337, 1.352, 1.334, 1.323]
postEE_VBF_0j    = [5.348, 2.477, 1.681, 1.395, 1.208, 1.165, 1.379, 1.470, 1.425, 1.396, 1.465, 1.274]
postEE_VBF_GTE1j = [5.889, 2.711, 1.946, 1.693, 1.520, 1.436, 1.384, 1.346, 1.337, 1.352, 1.334, 1.323]

preBPix_ggH_Inc   = [3.258, 1.545, 1.061, 0.914, 0.990, 1.206, 1.374, 1.420, 1.420, 1.410, 1.400, 1.358]
preBPix_ggH_0j    = [3.224, 1.496, 1.025, 0.805, 0.651, 0.552, 0.657, 1.396, 1.583, 1.506, 1.000, 1.000]
preBPix_ggH_GTE1j = [6.860, 3.264, 2.193, 1.817, 1.540, 1.411, 1.397, 1.412, 1.420, 1.416, 1.393, 1.379]
preBPix_VBF_Inc   = [5.847, 2.684, 1.997, 1.717, 1.543, 1.474, 1.426, 1.375, 1.360, 1.369, 1.347, 1.333]
preBPix_VBF_0j    = [5.530, 2.570, 1.703, 1.365, 1.205, 1.207, 1.419, 1.503, 1.455, 1.527, 1.567, 1.383]
preBPix_VBF_GTE1j = [6.320, 2.917, 2.063, 1.753, 1.569, 1.471, 1.416, 1.365, 1.354, 1.372, 1.357, 1.327]

postBPix_ggH_Inc   = [3.258, 1.545, 1.061, 0.914, 0.990, 1.206, 1.374, 1.420, 1.420, 1.410, 1.400, 1.358]
postBPix_ggH_0j    = [3.235, 1.518, 1.011, 0.796, 0.646, 0.524, 0.701, 1.469, 1.514, 1.326, 1.000, 1.000]
postBPix_ggH_GTE1j = [5.850, 3.247, 2.293, 1.859, 1.552, 1.411, 1.402, 1.420, 1.420, 1.410, 1.400, 1.358]
postBPix_VBF_Inc   = [5.847, 2.684, 1.997, 1.717, 1.543, 1.474, 1.426, 1.375, 1.360, 1.369, 1.347, 1.333]
postBPix_VBF_0j    = [5.537, 2.533, 1.747, 1.391, 1.200, 1.241, 1.429, 1.455, 1.465, 1.276, 1.561, 1.000]
postBPix_VBF_GTE1j = [6.262, 2.823, 2.123, 1.809, 1.574, 1.481, 1.426, 1.375, 1.360, 1.369, 1.347, 1.333]


simple_recoHpTCorrection = cs.Correction(
#simple_recoHpTCorrection = cs.CorrectionSet(
#    schema_version=2,
    name="recoHpTFactor",
    version=1,
    inputs=[
            cs.Variable(name="Reco. HpT", type="real", description="Reco. Higgs Transverse Momentum"),
            cs.Variable(name="nJet", type="string", description="number of jets: Inclusive (combined 0j, GTE1j), 0j, GTE1j"),
            cs.Variable(name="era", type="string", description="Era: 2022preEE, 2022postEE, 2023preBPix, 2023postBPix"),
            cs.Variable(name="process", type="string", description="ggH, VBF (for VH and ttH use VBF)"),
           ],
    output=cs.Variable(name="Factor", type="real", description="Correction Factor for Reco to Gen"),
    data=cs.Binning(
        nodetype="binning",
        input="Reco. HpT",
        edges=[0, 10, 20, 30, 40, 60, 80, 120, 200, 350, 450, 600, 9999],
        content=[3.2347999, 1.5181893, 1.0110607, 0.7962957, 0.64592665, 0.5238697, 0.7006475, 1.4689667, 1.5140077, 1.3264526, 1, 1],
        flow="clamp",
    ),
)
rich.print(simple_recoHpTCorrection)

lesssimple_recoHpTCorrection = cs.Correction(
    name="recoHpTFactor",
    version=1,
    inputs=[
            cs.Variable(name="Reco. HpT", type="real", description="Reco. Higgs Transverse Momentum"),
            cs.Variable(name="nJet", type="string", description="number of jets: Inclusive (combined 0j, GTE1j), 0j, GTE1j"),
            cs.Variable(name="era", type="string", description="Era: 2022preEE, 2022postEE, 2023preBPix, 2023postBPix"),
            cs.Variable(name="process", type="string", description="ggH, VBF (for VH and ttH use VBF)"),
           ],
    output=cs.Variable(name="Factor", type="real", description="Correction Factor for Reco to Gen"),
    data=cs.Category(
      nodetype="category",
      input="era",
      content=[
        cs.CategoryItem(
          key="2022preEE",
          value=cs.Category(
            nodetype="category",
            input="process",
            content=[
              cs.CategoryItem(
                key="ggH",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preEE_ggH_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preEE_ggH_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preEE_ggH_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              ), # end ggH CategoryItem
              cs.CategoryItem(
                key="VBF",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preEE_VBF_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preEE_VBF_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preEE_VBF_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              )
            ]
          )
        ), # closes preEE key
        cs.CategoryItem(
          key="2022postEE",
          value=cs.Category(
            nodetype="category",
            input="process",
            content=[
              cs.CategoryItem(
                key="ggH",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postEE_ggH_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postEE_ggH_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postEE_ggH_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              ), # end ggH CategoryItem
              cs.CategoryItem(
                key="VBF",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postEE_VBF_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postEE_VBF_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postEE_VBF_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              )
            ]
          )
        ), # closes postEE key
        cs.CategoryItem(
          key="2023preBPix",
          value=cs.Category(
            nodetype="category",
            input="process",
            content=[
              cs.CategoryItem(
                key="ggH",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preBPix_ggH_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preBPix_ggH_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preBPix_ggH_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              ), # end ggH CategoryItem
              cs.CategoryItem(
                key="VBF",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preBPix_VBF_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preBPix_VBF_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=preBPix_VBF_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              )
            ]
          )
        ), # closes preBPix key
        cs.CategoryItem(
          key="2023postBPix",
          value=cs.Category(
            nodetype="category",
            input="process",
            content=[
              cs.CategoryItem(
                key="ggH",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postBPix_ggH_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postBPix_ggH_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postBPix_ggH_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              ), # end ggH CategoryItem
              cs.CategoryItem(
                key="VBF",
                value=cs.Category(
                  nodetype="category",
                  input="nJet",
                  content=[
                    cs.CategoryItem(
                      key="Inclusive",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postBPix_VBF_Inc,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="0j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postBPix_VBF_0j,
                        flow="clamp",
                      )
                    ),
                    cs.CategoryItem(
                      key="GTE1j",
                      value=cs.Binning(
                        nodetype="binning",
                        input="Reco. HpT",
                        edges=global_edges,
                        content=postBPix_VBF_GTE1j,
                        flow="clamp",
                      ),
                    ),
                  ]
                ),
              )
            ]
          )
        ) # closes postBPix key
      ], # closes outermost "content" block, enclosing era keys
    ), # closes "data", which is the largest container for the correciton data
) # closes correction object

rich.print(lesssimple_recoHpTCorrection)

with open("mycorrections.json", "w") as fout:
    fout.write(lesssimple_recoHpTCorrection.json(exclude_unset=True))

import gzip

with gzip.open("mycorrections.json.gz", "wt") as fout:
    fout.write(lesssimple_recoHpTCorrection.json(exclude_unset=True))


