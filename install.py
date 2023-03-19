import launch
import os
import sys


def prepare_environment():
    torch_command = os.environ.get(
        "TORCH_COMMAND",
        "pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117",
    )

    sys.argv, skip_install = launch.extract_arg(sys.argv, "--skip-install")
    if skip_install:
        return

    sys.argv, skip_torch_cuda_test = launch.extract_arg(
        sys.argv, "--skip-torch-cuda-test"
    )
    sys.argv, reinstall_torch = launch.extract_arg(sys.argv, "--reinstall-torch")
    ngrok = "--ngrok" in sys.argv

    if (
        reinstall_torch
        or not launch.is_installed("torch")
        or not launch.is_installed("torchvision")
    ):
        launch.run(
            f'"{launch.python}" -m {torch_command}',
            "Installing torch and torchvision",
            "Couldn't install torch",
        )

    if not skip_torch_cuda_test:
        launch.run_python(
            "import torch; assert torch.cuda.is_available(), 'Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check'"
        )

    if not launch.is_installed("modelscope"):
        launch.run_pip(
            "install git+https://github.com/modelscope/modelscope.git@refs/pull/207/head",
            "modelscope",
        )

    if not launch.is_installed("pyngrok") and ngrok:
        launch.run_pip("install pyngrok", "ngrok")

    launch.run(
        f'"{launch.python}" -m pip install -r requirements.txt',
        desc=f"Installing requirements",
        errdesc=f"Couldn't install requirements",
    )


if __name__ == "__main__":
    prepare_environment()
