import matplotlib.font_manager
flist = [f.name for f in matplotlib.font_manager.fontManager.ttflist]

print(flist)