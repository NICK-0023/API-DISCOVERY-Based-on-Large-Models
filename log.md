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
2.主要步骤：     
01：注册Hugging Face，并申请模型访问权限，生成个人登录token  
02：在控制台安装Hugging Face-Hub并登录，开始下载Llama模型 （进行中 6%）
控制台命令如下：  
>huggingface-cli login  #登录  
>tokens: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

>huggingface-cli download meta-llama/Llama-2-7b --local-dir meta-llama/Llama-2-7b #下载  

03：安装 transformer（4.48.3）  accelerate  torch（进行中）  
04：运行脚本 LLM_Llama.py  
**2025/2/9**  
1.成功安装Meta Llama 3-8b 与 torch  
**2025/2/10**  
1.对Spark进行微调，并且完善输出格式  
2.利用GPT-4对50条RapidAPI进行推荐测试  
3.本地运行llama-3-8b时，内存以及显存不足，后续考虑更换轻量级模型 llama-2    
**2025/2/11**  
1.尝试下载llama-2后发现内存依然不足以支持运行，后续考虑在ollama平台上运行大模型。  
**2025/2/14**  
1.成功安装ollama  
2.成功安装llama3.2:1b 和 deepseek-r1:7b  
3.构建了实际使用场景数据    
**2015/2/14**  
1.成功安装bert  
2.正在安装llama模型  
3.准备安装openai提供的api调用  
**2025/2/16**  
1.正在安装llama2.7b.  
2.成功完成传统方法中的基于信息检索的方法并进行了初步实现  
3.准备安装llama3.2.1b和deepseek-r1  
4.正准备实现传统方法中的小规模网络的方法  
**2025/2/17**  
1.完成实现传统方法的小规模网络算法  
2.正在安装llama3.2.1b和deepseek-r1···  
3.成功安装llama2.7b  
**2025/2/25**  
1.ollama运行大模型的命令  
展示本地模型列表  
`D:\Ollama>ollama list`  
运行指定模型  
`D:\Ollama>ollama run deepseek-r1:7b`  
**2025\3\11** 
1.正在完善应用场景，预计构建50个应用场景，并人工完成正确映射数据集，进行结果比对。  
**2025\3\13**  
目前存在的问题：  
1.如何让LLM根据已有的RapidAPI数据集进行推荐,是否需要输入全部数据集构建上下文？  
2.如何构建合适的正确的场景与API的映射关系，是完全随机还是有意的构建具有相关功能API的场景（很大程度影响准确程度？）  
【例如：“场景一：根据用户的身高体重计算BMI健康值并给出健康建议--存在完全相同功能的API”  
        “场景二：根据用户的症状推荐相关药物并根据位置推荐附近的医院--存在部分功能的API“（人为取药物or医院？）  
        “场景三：根据用户的饮食习惯提出健康建议并且提出疾病隐患--不存在该功能的API”】  
3.实验是否可以只在某一个类别进行还是在全量条件下进行？  
解决方案：1.rag  2.LLM连接数据集  3.根据已知功能生成对应场景  
**2025\3\19**  
1.从五个类别中挑选了50个API描述构建场景  
**2025\3\21**  
1.构建完成50个应用场景的关键词
2.完成论文1-2章
3.下一步解决用本地模型连接数据库访问数据集  
**2025\3\24**  
1.成功使用python连接数据库并将数据输入给大模型(deepseek-r1:7b)结合用户输入进行推荐  
以下是具体推荐信息:
>请输入 API 关键词: social media

>=== LLM 推荐的 API ===
<think>
好的，我现在需要帮助用户找到与“social media”相关的API。让我先仔细看看用户提供的所有API列表，并找出哪些与社交媒体相关。
首先，列表中有许多不同的API，我得逐一查看每个API的功能，看是否有涉及社交媒体的。
现在分析用户的需求：寻找关于“social media”的API。需要考虑哪些API直接支持社交媒体内容生成、广告创建或用户互动等。
>- Social media caption（社交媒体文案）和Facebook Ad（生成Facebook广告）都明显涉及社交媒体。
>- Instagram live feed（Instagram直播）也属于社交媒体的一部分，但可能不是API服务本身。
>- 其他如工作相关的API（Workable, AdCopy AI）可能帮助创建广告，但也属于Google Ads的范畴。
>综合来看，Social media caption和Facebook Ad是最符合用户需求的。然而，考虑到用户更可能需要生成具体社交媒体内容，比如Instagram或Twitter文案，因此Social media caption可能是更好的选择。
></think>
根据您的需求，以下是推荐的相关API
1. **Social media caption**: 用于生成吸引人的社交媒体文案。
2. **Facebook Ad**: 生成Facebook广告，直接关联到社交平台的推广功能。
进程已结束,退出代码0   
2.存在的问题：  
①：本次测试仅仅使用了26个API作为查找的数据集，但是电脑性能已经到达瓶颈，后续必须要优化性能。  
②：后续需要优化用户输入提示  
③：是否可以使用网页版直接进行推荐