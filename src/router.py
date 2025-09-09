from langchain.chains.router import MultiPromptChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from llm import LLMClient

llm = LLMClient()

destinations = {
    "pr": {
        "description": "PR-отдел: посты, слоганы, хэштеги",
        "prompt": "prompts/pr.txt"
    },
    "sales": {
        "description": "Продажи: цена, преимущества, доставка",
        "prompt": "prompts/sales.txt"
    },
    "support": {
        "description": "Поддержка: вежливо, по-человечески",
        "prompt": "prompts/support.txt"
    }
}

destination_chains = {}
for role, info in destinations.items():
    with open(info["prompt"], encoding="utf-8") as f:
        tmpl = f.read()
    prompt = PromptTemplate.from_template(tmpl)
    destination_chains[role] = LLMChain(llm=llm, prompt=prompt)

router_chain = MultiPromptChain.from_llm(
    llm=llm,
    destination_chains=destination_chains,
    router_prompt_template="Ты маршрутизатор. Выбери роль: pr / sales / support. Вопрос: {input}",
    default_chain=destination_chains["support"],
    verbose=False
)
