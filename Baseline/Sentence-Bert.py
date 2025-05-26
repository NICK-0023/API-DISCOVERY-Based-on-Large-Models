from sentence_transformers import SentenceTransformer, util
import pandas as pd

print("正在加载 Sentence-BERT 模型...")
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L12-v2")
print("模型加载完成！")



file_paths = [
    'D:/Desktop/Papers/实验结果/Endpoint选择/Artificial Intelligence_Machine Learning.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Business.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Communication.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Data.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/eCommerce.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Education.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Finance.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Food.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/News, Media.xlsx',
    'D:/Desktop/Papers/实验结果/Endpoint选择/Video, Images.xlsx',
]
endpoint_names = [
"GET:Get List of Voices",
"POST:Generate Image",
"GET:/all_search by Security Term",
"POST:CreateImage",
"GET:Status",
"GET:/companies/{id}/people",
"GET:Property Sale Listings",
"POST:getDetailedReportByDay",
"GET:house-prices/get-sales-history",
"GET:properties/list-by-mls",
"POST:logout",
"GET:AccountList",
"POST:Create a dialogue",
"GET:Files",
"GET:getContacts",
"GET:Country Regions",
"GET:120 Hour Forecast",
"GET:/lookup-google",
"GET:Search",
"GET:Newest Companies in Category",
"GET:lookupSellerPrices",
"GET:products/search-by-barcode",
"GET:Item Info From Url",
"GET:Search By Category",
"GET:Materials",
"GET:Get word of the day from multiple sources",
"GET:/verse/{verse}",
"GET:getTotalActiveDays",
"POST:/memre_api/v1/study",
"GET:getClosestImage",
"GET:Stock News",
"GET:Most Visited",
"GET:market/news/{stock}",
"GET:Conversion Rates",
"GET:Stock News API",
"GET:Lookup a selection of 10 random cocktails",
"GET:Get user's diet for a specific day",
"GET:tips/list",
"GET:Search Grocery Products",
"GET:restaurants/get-info (Deprecated)",
"GET:Newswire Sri Lanka",
"GET:News",
"GET:Get all the year's top articles",
"GET:Get news for the entertainment.",
"GET:F1",
"GET:Search for Videos",
"GET:With RT Ratings",
"GET:Get Spanish Alt Text",
"POST:https://picnie.com/api/v1/create-image",
"POST:getSinglePhoto",

]
user_queries = [
    # 1. AI
    "Get list of voices",
    "Add prompt to image queue",
    "Search security info",
    "Generate image by prompt",
    "Check job status",

    # 2. Business
    "Company people info",
    "Search sale listings",
    "User daily report",
    "Sales history",
    "List properties by ID",

    # 3. Communication
    "Logout and QR screen",
    "List WhatsApp accounts",
    "Create dialogue",
    "Manage message attachments",
    "Recover contacts",

    # 4. Data
    "Find regions in country",
    "Weather forecast (up to 120h)",
    "Domain lookup via Google",
    "Twitter search results",
    "Newest companies by category",

    # 5. eCommerce
    "Offer lookup by product",
    "Search product by barcode",
    "Item info by Taobao URL",
    "Ikea products by categoryID",
    "Get materials",

    # 6. Education
    "Word of the day",
    "Get treasure by verse",
    "User active days in year",
    "Create user-item interaction",
    "Closest image metadata",

    # 7. Finance
    "Latest stock news",
    "Most visited cryptocurrencies",
    "Yahoo stock news",
    "Currency conversion rates",
    "Stock media content",

    # 8. Food
    "Random cocktail selection",
    "User diet plan by day",
    "Load food tips",
    "Search packaged foods",
    "Restaurant info",

    # 9. News
    "Sri Lanka news",
    "Movie news updates",
    "Top dev.to articles",
    "Entertainment news worldwide",
    "F1 top news",

    # 10. Video, Images
    "Search free videos",
    "Movie info with Rotten Tomatoes",
    "Pet image with Spanish alt text",
    "Single image by template",
    "Photo details"
]
# 3. 为每个用户查询计算相似度并输出 Top 10 匹配
reciprocal_ranks = []
hit_count = 0
top_n = 20

for i, query in enumerate(user_queries):
    file_index = int(i / 5)
    file_path = file_paths[file_index]
    print(f"读取文件：{file_path}")

    df = pd.read_excel(file_path)
    api_descriptions = df["Endpoint描述"].dropna().astype(str).tolist()
    api_names = df["Endpoint名称"].dropna().astype(str).tolist()
    print(f"\n用户查询 {i + 1}: {query}")

    # 使用 SBERT 生成嵌入
    embeddings = model.encode(api_descriptions + [query], convert_to_tensor=True)

    query_embedding = embeddings[-1]  # 最后一项是查询
    api_embeddings = embeddings[:-1]  # 前面的是所有 API 描述

    cosine_scores = util.cos_sim(query_embedding, api_embeddings).flatten()
    sorted_indices = cosine_scores.argsort(descending=True)

    top_k_names = [api_names[idx] for idx in sorted_indices[:top_n]]
    correct_api_name = endpoint_names[i]

    print(top_k_names)
    print(correct_api_name)

    if correct_api_name in top_k_names:
        rank = top_k_names.index(correct_api_name) + 1
        rr = 1 / rank
        hit_count += 1
    else:
        print("❌ 正确结果不在 Top-k 中")
        rr = 0.0

    reciprocal_ranks.append(rr)

    for rank, idx in enumerate(sorted_indices[:top_n], start=1):
        print(f"{rank}. 相似度：{cosine_scores[idx]:.4f}，Endpoint 名称：{api_names[idx]}")
    print('\n')

# 评估指标
mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)
hit_at_k = hit_count / len(user_queries)

print(f"Top-k = {top_n}")
print(f"MRR: {mrr:.4f}")
print(f"Hit@{top_n}: {hit_at_k:.4f}")