import time
import gradio as gr

from scripts.txt2video_synthesis import ui, shared


def on_ui_tabs():
    with gr.Blocks() as block:
        ui.create_ui()

    return [(block, "Text2Video synthesis", "text2video_synthesis")]


def wait_on_server():
    while 1:
        time.sleep(0.5)


def launch():
    block, _, _ = on_ui_tabs()[0]

    if shared.cmd_opts.ngrok is not None:
        import scripts.txt2video_synthesis.ngrok as ngrok

        address = ngrok.connect(
            shared.cmd_opts.ngrok,
            shared.cmd_opts.port if shared.cmd_opts.port is not None else 7860,
            shared.cmd_opts.ngrok_region,
        )
        print("Running on ngrok URL: " + address)

    app, local_url, share_url = block.launch(
        share=shared.cmd_opts.share,
        server_port=shared.cmd_opts.port,
        server_name=shared.cmd_opts.host,
        prevent_thread_lock=True,
    )

    wait_on_server()


if shared.is_webui_extension():
    from modules import script_callbacks

    script_callbacks.on_ui_tabs(on_ui_tabs)
