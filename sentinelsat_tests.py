from pathlib import Path
from collections import OrderedDict
from sentinelsat import SentinelAPI


def get_env_data_as_dict(path: Path) -> dict:
    with open(path, 'r') as f:
        return dict(tuple(line.replace('\n', '').split('=')) for line
                    in f.readlines() if not line.startswith('#'))


def main():
    auth = get_env_data_as_dict(Path("./.env"))
    api = SentinelAPI(auth["COPERNICUS_USERNAME"], auth["COPERNICUS_PASSWORD"], api_url='https://scihub.copernicus.eu/dhus/')

    tiles = ['33VUC', '33UUB']

    query_kwargs = {
        'platformname': 'Sentinel-2',
        'producttype': 'S2MSI1C',
        'date': ('NOW-14DAYS', 'NOW')}

    products = OrderedDict()
    for tile in tiles:
        kw = query_kwargs.copy()
        kw['tileid'] = tile
        pp = api.query(**kw)
        products.update(pp)

    api.download_all(products)


if __name__ == "__main__":
    main()
