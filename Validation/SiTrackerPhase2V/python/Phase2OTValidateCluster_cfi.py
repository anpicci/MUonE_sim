import FWCore.ParameterSet.Config as cms

from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer

clusterValid = DQMEDAnalyzer('Phase2OTValidateCluster',
    Verbosity = cms.bool(False),
    TopFolderName = cms.string("TrackerPhase2Clusters"),
    PixelPlotFillingFlag =cms.bool(False),
    ClusterSource = cms.InputTag("siPhase2Clusters"),
    InnerPixelClusterSource = cms.InputTag("siPixelClusters"),
    OuterTrackerDigiSimLinkSource = cms.InputTag("simSiPixelDigis", "Tracker"),
    InnerPixelDigiSimLinkSource = cms.InputTag("simSiPixelDigis", "Pixel"), 
    PSimHitSource  = cms.VInputTag('g4SimHits:TrackerHitsPixelBarrelLowTof',
                                   'g4SimHits:TrackerHitsPixelBarrelHighTof',
                                   'g4SimHits:TrackerHitsPixelEndcapLowTof',
                                   'g4SimHits:TrackerHitsPixelEndcapHighTof',
                                   'g4SimHits:TrackerHitsTIBLowTof',
                                   'g4SimHits:TrackerHitsTIBHighTof',
                                   'g4SimHits:TrackerHitsTIDLowTof',
                                   'g4SimHits:TrackerHitsTIDHighTof',
                                   'g4SimHits:TrackerHitsTOBLowTof',
                                   'g4SimHits:TrackerHitsTOBHighTof',
                                   'g4SimHits:TrackerHitsTECLowTof',
                                   'g4SimHits:TrackerHitsTECHighTof'),
    simtracks = cms.InputTag("g4SimHits"),
    SimTrackMinPt = cms.double(0.),
    ECasRings = cms.bool(True),
    GeometryType = cms.string('idealForDigi'),
    ZRPositionMapH = cms.PSet(
      NxBins = cms.int32(6000),
      xmin = cms.double(-300.),
      xmax = cms.double(300.),
      NyBins = cms.int32(1200),
      ymin = cms.double(0.),
      ymax = cms.double(120.),
      switch = cms.bool(True)
      ),
    SimZRPositionMapH = cms.PSet(
      NxBins = cms.int32(6000),
      xmin = cms.double(-300.),
      xmax = cms.double(300.),
      NyBins = cms.int32(1200),
      ymin = cms.double(0.),
      ymax = cms.double(120.),
      switch = cms.bool(True)
      ),
    XYPositionMapH = cms.PSet(
      NxBins = cms.int32(2400),
      xmin = cms.double(-120.),
      xmax = cms.double(120.),
      NyBins = cms.int32(2400),
      ymin = cms.double(-120.),
      ymax = cms.double(120.),
      switch = cms.bool(True)
      ),
    XYBarrelPositionMapH = cms.PSet(
      NxBins = cms.int32(2400),
      xmin = cms.double(-120.),
      xmax = cms.double(120.),
      NyBins = cms.int32(2400),
      ymin = cms.double(-120.),
      ymax = cms.double(120.),
      switch = cms.bool(True)
      ),
    XYGlobalPositionMapH = cms.PSet(
      NxBins = cms.int32(200),
      xmin = cms.double(-50.),
      xmax = cms.double(50.),
      NyBins = cms.int32(100),
      ymin = cms.double(-50.),
      ymax = cms.double(50.),
      switch = cms.bool(True)
      ),
    XYLocalPositionMapH = cms.PSet(
      NxBins = cms.int32(1024),
      #NxBins = cms.int32(50),
      #xmin = cms.double(-10.),
      #xmax = cms.double(10.),
      xmin = cms.double(-4.6),
      xmax = cms.double(4.6),
      NyBins = cms.int32(10),
      ymin = cms.double(-2.),
      ymax = cms.double(2.),
      switch = cms.bool(True)
      ),
    XYEndCapPositionMapH = cms.PSet(
      NxBins = cms.int32(2400),
      xmin = cms.double(-120.),
      xmax = cms.double(120.),
      NyBins = cms.int32(2400),
      ymin = cms.double(-120.),
      ymax = cms.double(120.),
      switch = cms.bool(True)
      ),
    ClusterSize = cms.PSet(
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      switch = cms.bool(True)
      ),
    ClusterCharge = cms.PSet(
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      switch = cms.bool(True)
      ),
    Delta_X_Strip = cms.PSet(
      NxBins = cms.int32(50),
      xmin = cms.double(-0.01),
      xmax = cms.double(0.01),
      #xmin = cms.double(-3.),
      #xmax = cms.double(3.),
      switch = cms.bool(True)
      ),
    Delta_X_Pixel = cms.PSet(
      NxBins = cms.int32(50),
      xmin = cms.double(-0.01),
      xmax = cms.double(0.01),
      #xmin = cms.double(-3.),
      #xmax = cms.double(3.),
      switch = cms.bool(True)
      ),
    Delta_Y_Strip = cms.PSet(
      NxBins = cms.int32(70),
      xmin = cms.double(-1.4),
      xmax = cms.double(1.4),
      #xmin = cms.double(-3.),
      #xmax = cms.double(3.),
      switch = cms.bool(True)
      ),
    Delta_Y_Pixel = cms.PSet(
      NxBins = cms.int32(75),
      xmin = cms.double(-0.15),
      xmax = cms.double(0.15),
      switch = cms.bool(True)
      ),
    Delta_X_Strip_P = cms.PSet(
      NxBins = cms.int32(50),
      xmin = cms.double(-0.01),
      xmax = cms.double(0.01),
      #xmin = cms.double(-3.),
      #xmax = cms.double(3.),
      switch = cms.bool(True)
      ),
    Delta_X_Pixel_P = cms.PSet(
      NxBins = cms.int32(50),
      xmin = cms.double(-0.01),
       xmax = cms.double(0.01),
      #xmin = cms.double(-3.),
      #xmax = cms.double(3.),
      switch = cms.bool(True)
      ),
    Delta_Y_Strip_P = cms.PSet(
      NxBins = cms.int32(70),
      #xmin = cms.double(-0.2),
      #xmax = cms.double(0.2),
      xmin = cms.double(-1.4),
      xmax = cms.double(-1.4),
      switch = cms.bool(True)
      ),
    Delta_Y_Pixel_P = cms.PSet(
        NxBins = cms.int32(75),
      xmin = cms.double(-0.15),
      xmax = cms.double(0.15),
      #xmin = cms.double(-3.),
      #xmax = cms.double(3.),
      switch = cms.bool(True)
      ),
    Primary_Digis_Strip = cms.PSet(
      NxBins = cms.int32(100),
      xmin = cms.double(0.),
      xmax = cms.double(1000.),
      switch = cms.bool(True)
      ),
    Primary_Digis_Pixel = cms.PSet(
      NxBins = cms.int32(100),
      xmin = cms.double(0.),
      xmax = cms.double(1000.),
      switch = cms.bool(True)
      ),
    Other_Digis_Strip = cms.PSet(
      NxBins = cms.int32(100),
      xmin = cms.double(0.),
      xmax = cms.double(1000.),
      switch = cms.bool(True)
      ),
    Other_Digis_Pixel = cms.PSet(
      NxBins = cms.int32(100),
      xmin = cms.double(0.),
      xmax = cms.double(1000.),
      switch = cms.bool(True)
      )
    )

