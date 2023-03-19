import gradio as gr

from scripts.txt2video_synthesis.generate import (
    load_pipeline,
    unload_pipeline,
    generate,
)


def load_pipeline_w():
    load_pipeline()
    return gr.update(visible=True), gr.update(visible=False)


def unload_pipeline_w():
    unload_pipeline()
    return gr.update(visible=False), gr.update(visible=True)


def create_ui():
    with gr.Row():
        with gr.Column():
            with gr.Row():
                load_button = gr.Button("Load pipeline", variant="primary")
                unload_button = gr.Button("Unload pipeline")
            with gr.Row(visible=False) as main:
                generate_button = gr.Button("Generate", variant="konsoprimary")
                with gr.Row():
                    prompt = gr.Text(label="Prompt", max_lines=1)
                    seed = gr.Number(label="seed", value=-1)
                with gr.Column():
                    video = gr.Video(label="Result")
            with gr.Row(visible=True) as notLoaded:
                gr.Text("Click 'Load pipeline'.")

    load_button.click(fn=load_pipeline_w, outputs=[main, notLoaded])
    unload_button.click(fn=unload_pipeline_w, outputs=[main, notLoaded])
    generate_button.click(fn=generate, inputs=[prompt, seed], outputs=[video])
