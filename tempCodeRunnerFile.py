query = input("Enter your query: ")
while(query!='exit'):
    output = chain.invoke({"query": query})
    print(output.content)

    memory.save_context({"query": query}, {"output": output.content})
    query = input("Enter your query: ")