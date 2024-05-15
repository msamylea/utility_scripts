from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.runnables import RunnableLambda

from tool_defs import scrape_internet
import json

     
model = OllamaFunctions(model="l3custom", format="json")

model = model.bind_tools(
    tools = [
        { 
            "name": "scrape_internet",
            "description": "Search the internet for information on a given topic",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query used to search the internet"
                    }
                },
                "required": ["query"]
            }
        },
    ]   
)



functions = {
    "scrape_internet": scrape_internet,
}


def invoke_and_run(model, invoke_arg):
    result = model.invoke(invoke_arg)
    print(result)
    if result:
        function_call = result.additional_kwargs['function_call']
        print(function_call)
        function_name = function_call['name']
        arguments = json.loads(function_call['arguments'])
        function = functions[function_name]
        if function_name == 'scrape_internet':
            runnable = RunnableLambda(function)
            query = arguments['query']
            if isinstance(query, str):
                runnable.invoke(query)
            else:
                runnable.map().invoke(query)
       
            function(**arguments)


invoke_and_run(model, "What is the current stock price of Apple (AAPL)?")
