import yaml

with open('market_coords_cfg.YAML') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

xx = 1