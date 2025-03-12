import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm  # 进度条

def batch_translate(text_list):
    """批量翻译列表中的文本"""
    translator = GoogleTranslator(source='auto', target='zh-CN')
    return [translator.translate(text) if pd.notna(text) else '' for text in tqdm(text_list, desc="翻译中")]

def process_api_csv(  input_csv, output_xlsx):
    df = pd.read_csv(input_csv)
    df = df[['API名称', 'API描述']]

    # 批量翻译
    df['中文翻译'] = batch_translate(df['API描述'].tolist())

    # 保存为Excel文件
    df.to_excel(output_xlsx, index=False)
    print(f"✅ 处理完成，已保存到 {output_xlsx}")

# 运行
input_csv = 'Weather.csv'
output_xlsx = 'translated_api_data_Weather.xlsx'
process_api_csv(input_csv, output_xlsx)
