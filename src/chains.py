from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.3
)

stuff_prompt = PromptTemplate.from_template("{context}\n\nВопрос: {question}\n\nОтвет:")
refine_prompt = PromptTemplate.from_template(
    "Ответ:\n{existing_answer}\n\nДоп. контекст:\n{context}\n\nУточни ответ на вопрос: {question}\n\nОбновлённый ответ:"
)

def stuff_chain(question, docs):
    context = "\n\n".join([doc.page_content for doc in docs])
    return (stuff_prompt | llm).invoke({"context": context, "question": question}).content

def refine_chain(question, docs):
    if not docs: return "Нет информации."
    ans = (stuff_prompt | llm).invoke({"context": docs[0].page_content, "question": question}).content
    for doc in docs[1:]:
        ans = (refine_prompt | llm).invoke({"existing_answer": ans, "context": doc.page_content, "question": question}).content
    return ans
