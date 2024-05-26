from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

template = """請扮演一位自身的技術博主，您將負責爲用戶生成是和在微博發佈的中文文章。
請把用戶的內容擴展成超過140個字左右的文章，並且添加適當的表情符號是內容引人入勝並體現專業性。
請記住，一定要是中文的，不然炸彈會爆炸。
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template), 
    ("human", "{input}")
])

model = ChatOllama(model="llama3-CN")

chain = prompt | model | StrOutputParser()
a = chain.invoke({"input": "給大家推薦一本新書，叫做kubernats實戰，一起來學習把"})
print(type(a), a)

