# Lazy imports to avoid pulling in heavy deps (omnidata_tools, open3d) at plugin load time.
# nerfstudio's plugin system imports this module; we defer data parser imports until accessed.

def __getattr__(name):
    _lazy_map = {
        'CoolerMapDataParserSpecification': '.data.coolermap_dataparser',
        'GSDFStudioDataParserSpecification': '.data.g_sdfstudio_dataparser',
        'MushroomDataParserSpecification': '.data.mushroom_dataparser',
        'NormalNerfstudioSpecification': '.data.normal_nerfstudio',
        'NRGBDDataParserSpecification': '.data.nrgbd_dataparser',
        'ReplicaDataParserSpecification': '.data.replica_dataparser',
        'ScanNetppDataParserSpecification': '.data.scannetpp_dataparser',
    }
    if name in _lazy_map:
        import importlib
        mod = importlib.import_module(_lazy_map[name], package=__name__)
        obj = getattr(mod, name)
        globals()[name] = obj  # cache for next access
        return obj
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "__version__",
    "MushroomDataParserSpecification",
    "ReplicaDataParserSpecification",
    "GSDFStudioDataParserSpecification",
    "NRGBDDataParserSpecification",
    "ScanNetppDataParserSpecification",
    "CoolerMapDataParserSpecification",
    "NormalNerfstudioSpecification",
]
