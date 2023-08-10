import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    AzureTextCompletion,
    OpenAITextCompletion,
)
from semantic_kernel.orchestration.context_variables import ContextVariables

useAzureOpenAI = True
model = "text-davinci-003"

def main():
    kernel = sk.Kernel()

    # Configure AI service used by the kernel. Load settings from the .env file.
    if useAzureOpenAI:
        deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
        kernel.add_text_completion_service(
            "dv", AzureTextCompletion(deployment, endpoint, api_key)
        )
    else:
        api_key, org_id = sk.openai_settings_from_dot_env()
        kernel.add_text_completion_service(
            "dv", OpenAITextCompletion(model, api_key, org_id)
        )

    skills_directory = "skills"

    fun_skill = kernel.import_semantic_skill_from_directory(
        skills_directory, "AuthoringSkill"
    )

    explanation_function = fun_skill["Explanation"]

    # The "input" variable in the prompt is set by "content" in the ContextVariables object.
    context_variables = ContextVariables(
        content="Generative AI", variables={"style": "descriptive professional academic"}
    )
    result = explanation_function(variables=context_variables)

    print(result)

    # You can also invoke functions like this
    # result = await explanation_function.invoke_async("Generative AI")
    # print(result)


if __name__ == "__main__":
    main()
