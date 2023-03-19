import gradio as gr

from modules import script_callbacks

from scripts.txt2video_synthesis import ui


def on_ui_tabs():
    with gr.Blocks() as block:
        ui.create_ui()

    return [(block, "Text2Video synthesis", "text2video_synthesis")]


script_callbacks.on_ui_tabs(on_ui_tabs)