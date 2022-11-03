from enum import Enum


class EGSProductType(Enum):
    PRODUCT_ENGINE = "engines"  #: Engines for developing games
    PRODUCT_GAME = "games"  #: Games
    PRODUCT_BUNDLE = "bundles"  #: An EGS bundle
    ALL_PRODUCTS = "|".join([
        PRODUCT_ENGINE,
        PRODUCT_GAME,
        PRODUCT_BUNDLE
    ])  #: All possible products
