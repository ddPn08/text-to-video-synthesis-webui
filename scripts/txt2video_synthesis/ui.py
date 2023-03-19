import gradio as gr

from scripts.txt2video_synthesis.generate import (
    load_pipeline,
    unload_pipeline,
    generate,
)


def load_pipeline_w():
    load_pipeline()
    return gr.update(visible=True), "Pipeline loaded"


def unload_pipeline_w():
    unload_pipeline()
    return gr.update(visible=False), "Pipeline unloaded"


def create_ui():
    with gr.Row():
        with gr.Column():
            status = gr.Textbox(show_label=False, value="")
            with gr.Row():
                load_button = gr.Button("Load pipeline", variant="primary")
                unload_button = gr.Button("Unload pipeline")
            with gr.Box(visible=False) as main:
                with gr.Row().style(equal_height=False):
                    with gr.Column():
                        prompt = gr.Text(label="Prompt", max_lines=1)
                        seed = gr.Number(label="seed", value=-1)
                    with gr.Column() as c:
                        c.scale = 0.5
                        generate_button = gr.Button("Generate", variant="primary")
                with gr.Column():
                    video = gr.Video(label="Result")

    load_button.click(fn=load_pipeline_w, outputs=[main, status])
    unload_button.click(fn=unload_pipeline_w, outputs=[main, status])
    generate_button.click(fn=generate, inputs=[prompt, seed], outputs=[video])
