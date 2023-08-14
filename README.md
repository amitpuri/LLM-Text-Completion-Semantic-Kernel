# LLM-Text-Completion using Semantic-Kernel

The `sk-python-Text-Completion` console application demonstrates how to execute a semantic function.

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 and above
  - [Poetry](https://python-poetry.org/) is used for packaging and dependency management
  - [Semantic Kernel Tools](https://marketplace.visualstudio.com/items?itemName=ms-semantic-kernel.semantic-kernel)

## Configuring the starter

The starter can be configured with a `.env` file in the project which holds api keys and other secrets and configurations.

Make sure you have an
[Open AI API Key](https://openai.com/api/) or
[Azure Open AI service key](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?pivots=rest-api)

Copy the `.env.example` file to a new file named `.env`. Then, copy those keys into the `.env` file:

```
OPENAI_API_KEY=""
OPENAI_ORG_ID=""
AZURE_OPENAI_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
```

## Running the starter

To run the console application within Visual Studio Code, just hit `F5`.
As configured in `launch.json` and `tasks.json`, Visual Studio Code will run `poetry install` followed by `python text_completion/main.py`

To build and run the console application from the terminal use the following commands:

```powershell
poetry install
poetry run python text_completion/main.py
```

# Sample output

TARGET AUDIENCE:
AI enthusiasts, developers, and researchers.

+++++

PURPOSE:
The purpose of this article is to explain the concept of Generative AI to the target audience. The article will provide a detailed explanation of Generative AI, its applications, and how it works. The article will also provide examples of Generative AI in real-world scenarios.

+++++

LENGTH:
1000 words

Generative AI: A Comprehensive Guide

Artificial Intelligence (AI) has been a buzzword for the past few years, and it has been transforming the way we live and work. AI has been used in various fields, including healthcare, finance, and entertainment. One of the most exciting areas of AI is Generative AI. In this article, we will explore Generative AI, its applications, and how it works.

What is Generative AI?

Generative AI is a type of AI that can create new data that is similar to the data it has been trained on. It is a subset of machine learning that uses deep neural networks to generate new data. Generative AI can be used to create images, videos, music, and even text. It is a powerful tool that can be used in various fields, including art, design, and entertainment.

How does Generative AI work?

Generative AI works by using deep neural networks to learn the patterns in the data it has been trained on. The neural network consists of layers of nodes that are connected to each other. Each node in the network performs a simple mathematical operation on the input data and passes the result to the next layer. The output of the last layer is the generated data.

The neural network is trained on a dataset that contains examples of the data that it needs to generate. For example, if we want to generate images of cats, we would train the neural network on a dataset of cat images. During training, the neural network learns the patterns in the data and uses them to generate new data that is similar to the training data.

Applications of Generative AI

Generative AI has many applications in various fields. Some of the most exciting applications of Generative AI are:

1. Art and Design: Generative AI can be used to create art and design. It can generate images, videos, and music that are unique and creative.

2. Gaming: Generative AI can be used to create game content, such as levels, characters, and items.

3. Healthcare: Generative AI can be used to generate synthetic data that can be used to train medical models. This can help in the development of new drugs and treatments.

4. Finance: Generative AI can be used to generate synthetic financial data that can be used to train financial models. This can help in predicting stock prices and other financial indicators.

Examples of Generative AI

1. StyleGAN: StyleGAN is a Generative AI model that can generate high-quality images of faces. It was developed by NVIDIA and has been used in various applications, including art and design.

2. GPT-3: GPT-3 is a Generative AI model that can generate human-like text. It was developed by OpenAI and has been used in various applications, including chatbots and language translation.

3. DeepDream: DeepDream is a Generative AI model that can generate images that are surreal and dream-like. It was developed by Google and has been used in various applications, including art and design.

Conclusion

Generative AI is a powerful tool that can be used in various fields, including art, design, and entertainment. It works by using deep neural networks to learn the patterns in the data it has been trained on and generate new data that is similar to the training data. Generative AI has many applications, including art and design, gaming, healthcare, and finance. With the development of new Generative AI models, we can expect to see more exciting applications of Generative AI in the future.

References:

1. https://www.nvidia.com/en-us/research/ai-playground
2. https://openai.com/blog/gpt-3-apps
3. https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html

Further, simplify using LangChain
- [Text Completion via LangChain](https://github.com/amitpuri/LLM-Text-Completion-langchain)
- [Text Completion via OpenAI Python](https://github.com/amitpuri/LLM-Text-Completion)
- [Semantic Kernel Starters](https://github.com/microsoft/semantic-kernel-starters)
  
More comprehensive demos are available on [LLM Scenarios, Use cases on the Gradio app](https://github.com/amitpuri/ask-picturize-it)

