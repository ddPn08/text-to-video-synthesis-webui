import launch

if not launch.is_installed("modelscope"):
    launch.run_pip("install modelscope", "modelscope")
