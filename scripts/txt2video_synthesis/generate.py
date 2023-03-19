import os
from pathlib import Path
import torch
import random
from scripts.txt2video_synthesis.shared import ROOT_DIR
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from huggingface_hub import snapshot_download

pipe = None

def load_pipeline():
    global pipe

    if pipe is not None:
        return

    model_dir = Path(os.path.join(ROOT_DIR, "models"))
    cache_dir = Path(os.path.join(ROOT_DIR, "cache"))
    snapshot_download(
        "damo-vilab/modelscope-damo-text-to-video-synthesis",
        repo_type="model",
        local_dir=model_dir,
        cache_dir=cache_dir,
        local_dir_use_symlinks=False,
    )
    pipe = pipeline("text-to-video-synthesis", model_dir.as_posix())

    print("Loaded pipeline.")


def unload_pipeline():
    global pipe
    del pipe
    pipe = None
    print("Unloaded pipeline.")


def generate(prompt: str, seed: int):
    if seed == -1:
        seed = random.randint(0, 1000000)
    torch.manual_seed(seed)
    return pipe({"text": prompt})[OutputKeys.OUTPUT_VIDEO]
