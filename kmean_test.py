from utils.autoanchor import kmean_anchors
# anchors = kmean_anchors(dataset="data/nuscenes.yaml", n=9, img_size=416)
# print("Generated Anchors:", anchors)
kmean_anchors(dataset="data/nuscenes.yaml", n=3, img_size=416, thr=3.5, gen=500, verbose=True)