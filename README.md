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
Sample output

TARGET AUDIENCE AGE:
18-50

+++++
TARGET AUDIENCE INTEREST:
Technology, AI, Machine Learning, Data Science, Computer Science, Programming, Robotics, Automation, Innovation, Creativity, Future, Science Fiction, Gaming, Entertainment, Social Media, Business, Marketing, Education, Career, Entrepreneurship, Finance, Health, Lifestyle, Travel, Food, Culture, Sports, News, Politics, Environment, Philosophy, Psychology, Spirituality, Religion, History, Art, Design, Fashion, Beauty, Parenting, Family, Relationships, Self-Improvement, Motivation, Inspiration, Personal Development, Society, Global Issues, Human Rights, Charity, Volunteering, Non-Profit, etc.

+++++
TARGET AUDIENCE LOCATION:
Worldwide

+++++
CONTENT LENGTH:
1000-1500 words

+++++
LANGUAGE:
English

+++++
PURPOSE:
To educate and inform the audience about Generative AI, its applications, benefits, challenges, and future prospects. To inspire and encourage the audience to explore and learn more about AI, Machine Learning, and Data Science. To promote the importance of ethical and responsible use of AI for the betterment of humanity and the planet. To provide valuable insights and resources for the audience to enhance their knowledge and skills in AI-related fields. To foster a culture of innovation, creativity, and collaboration in the global AI community. To contribute to the advancement of science and technology for the benefit of all.

+++++
REFERENCES:
Please provide credible sources and references to support the content. Use APA style for in-text citations and references.

+++++
DEADLINE:
7 days from the start date

+++++
BUDGET:
$100-150

+++++
ADDITIONAL NOTES:
Please provide a clear and concise title, subheadings, and bullet points to organize the content. Use simple and easy-to-understand language, avoid jargon and technical terms as much as possible. Use visuals, diagrams, and examples to illustrate the concepts and ideas. Use active voice and avoid passive voice. Use short sentences and paragraphs. Use transition words and phrases to connect the ideas and make the content flow smoothly. Use headings and subheadings to break down the content into sections. Use bold, italic, and underline to highlight the key points. Use numbered and bulleted lists to summarize the information. Use hyperlinks to provide additional resources and references. Use a friendly and engaging tone to connect with the audience. Use humor and storytelling to make the content more interesting and memorable. Use a conclusion to summarize the main points and provide a call to action for the audience. Use a bio to introduce yourself and your expertise in the field. Use a disclaimer to clarify that the content is for educational and informational purposes only and not intended to provide professional advice or services. Use a feedback form to collect feedback and suggestions from the audience. Use a contact form to provide contact information for further inquiries and collaborations. Use a social media share button to encourage the audience to share the content on their social media platforms. Use a copyright notice to protect the content from unauthorized use and reproduction. Use a privacy policy to protect the audience's personal information and data. Use a terms of use to clarify the terms and conditions of using the website and the content. Use a disclaimer to clarify that the website and the content are provided as is and without any warranties or guarantees. Use a contact form to provide contact information for technical support and customer service. Use a FAQ section to answer frequently asked questions. Use a search bar to help the audience find the content they are looking for. Use a navigation menu to help the audience navigate the website and the content. Use a responsive design to ensure that the website and the content are accessible and user-friendly on all devices and platforms. Use a fast loading speed to ensure that the website and the content load quickly and smoothly. Use a secure connection to ensure that the website and the content are safe and protected from cyber threats and attacks. Use a backup and recovery system to ensure that the website and the content are backed up and recoverable in case of any data loss or corruption. Use a content management system to ensure that the website and the content are easy to manage and update. Use a web analytics tool to track and analyze the website traffic and user behavior. Use a search engine optimization tool to optimize the website and the content for search engines and improve the visibility and ranking of the website. Use a social media marketing tool to promote the website and the content on social media platforms and increase the reach and engagement of the audience. Use an email marketing tool to send newsletters and updates to the audience and keep them informed and engaged. Use a customer relationship management tool to manage and nurture the relationships with the audience and provide personalized and relevant content and services. Use a project management tool to manage and coordinate the content creation and publishing process and ensure that the content is delivered on time and within budget. Use a collaboration tool to facilitate communication and collaboration among the content
