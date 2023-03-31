import yaml

data_yaml = dict(
    train = '../archive/train',
    val = '../archive/valid',
    nc = 1,
    names = ['Tire']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)