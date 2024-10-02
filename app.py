import json
import gradio as gr

# 从 JSON 文件中加载数据
def load_options_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['models']

# 将选择保存到新的 JSON 文件
def save_choices_to_json(choice1, choice2):
    choices = {
        "selected_choice_1": choice1,
        "selected_choice_2": choice2
    }
    with open('output.json', 'w') as file:
        json.dump(choices, file, indent=4)
    return "Choices saved to output.json"

# 加载选项
options1 = load_options_from_json('config.json')
options2 = load_options_from_json('config.json')

# 创建 Gradio 界面
with gr.Blocks() as demo:
    gr.Markdown("# Select Options and Save")
    
    # 第一个下拉菜单
    dropdown1 = gr.Dropdown(label="Select Option from File 1", choices=options1)
    
    # 第二个下拉菜单
    dropdown2 = gr.Dropdown(label="Select Option from File 2", choices=options2)
    
    # 保存按钮及回调函数
    button = gr.Button("Save Choices")
    button.click(fn=save_choices_to_json, inputs=[dropdown1, dropdown2], outputs=gr.Textbox())

# 启动 Gradio 应用
demo.launch()