### 工作日志
**2025/2/7**  
1.成功调用了星火大模型API  
（Spark Lite - 无限使用）  
（Spark4.0 Ultra -  2000000 tokens）  
代码文件 ../LLM_Spark.py
网址 https://www.xfyun.cn/    
接口文档 https://www.xfyun.cn/doc/spark/HTTP%E8%B0%83%E7%94%A8%E6%96%87%E6%A1%A3.html#_1-%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E
**2025/2/8**  
1.开始安装Meta Llama模型
操作文档 https://www.llama.com/docs/llama-everywhere/running-meta-llama-on-windows/  
主要步骤：
01：注册Hugging Face，并申请模型访问权限，生成个人登录token
02：在控制台安装Hugging Face-Hub并登录，开始下载Llama模型  
>huggingface-cli login  #登录  

>huggingface-cli download meta-llama/Meta-Llama-3-8B-Instruct --include "original/*" --local-dir meta-llama/Meta-Llama-3-8B-Instruct #下载

03：安装 transformer torch accelerate  
04：运行脚本 LLM_Llama.py  

