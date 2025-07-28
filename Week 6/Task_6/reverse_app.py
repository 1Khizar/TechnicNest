import gradio as gr

def reverse_sentence(sentence):
    return sentence[::-1]

iface = gr.Interface(fn=reverse_sentence, inputs="text", outputs="text",
                     title="Reverse Sentence",
                     description="Enter a sentence to get it reversed.")

iface.launch()
