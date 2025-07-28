import gradio as gr

def square_number(num):
    return num * num

iface = gr.Interface(fn=square_number, inputs="number", outputs="number", 
                     title="Square Calculator",
                     description="Enter a number to get its square.")

iface.launch()
