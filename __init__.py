from .nodes.hf.hf_download import HFDownloader
from .nodes.auto.downloader import AutoModelDownloader
from .nodes.cai.cai_download import CivitAIDownloader
import os

# Node mappings
NODE_CLASS_MAPPINGS = { 
    "HF Downloader": HFDownloader,
    "Auto Model Downloader": AutoModelDownloader,
    "CivitAI Downloader": CivitAIDownloader,
}

# Display names
NODE_DISPLAY_NAME_MAPPINGS = { 
    "HF Downloader": "HF Download",
    "Auto Model Downloader": "Auto Model Finder (Experimental)",
    "CivitAI Downloader": "CivitAI Download",
}

# Web directory for JavaScript files
WEB_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY"
]
import subprocess
import importlib.util
import folder_paths
import shutil
import sys
import traceback

from  .efficiency_nodes import NODE_CLASS_MAPPINGS
#from  .py.ttl_nn_latent_upscaler import NODE_CLASS_MAPPINGS
#from  .py.city96_latent_upscaler import NODE_CLASS_MAPPINGS


WEB_DIRECTORY = "js"

CC_VERSION = 2.0

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'CC_VERSION']
