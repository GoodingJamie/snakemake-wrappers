from array import array
import ROOT as R

for filename in snakemake.output:
    tfile = R.TFile(filename, "RECREATE")
    ttree = R.TTree("TestTree", "TestTree")

    # Define variables #
    px  = array('d',[0])
    py = array('d',[0])
    pz = array('d',[0])
    pt = array('d',[0])
    p = array('d',[0])
    
    # Define branches from variables #
    ttree.Branch("px", px, 'px/D')
    ttree.Branch("py", py, 'py/D')
    ttree.Branch("pz", pz, 'pz/D')
    ttree.Branch("pt", pt, 'pt/D')
    ttree.Branch("p", p, 'p/D')

    # Fill tree #
    for i in range(100):
        px[0] = R.gRandom.Gaus(1000, 40)
        py[0] = R.gRandom.Gaus(1000, 40)
        pz[0] = R.gRandom.Gaus(20000, 800)

        pt[0] = px[0]**2 + py[0]**2
        p[0] = pt[0]**2 + pz[0]**2

        ttree.Fill()
    tfile.Write()
    tfile.Close()
