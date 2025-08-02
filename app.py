import boto3
import botocore.config

def blog_generate_using_bedrock(blogtopic:str)-> str:
    prompt=f"""<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]
    """

    body={
        "prompt":prompt,
        "max_gen_len":512,
        "temperature":0.5,
        "top_p":0.9
    }

    try:
        bedrock=boto3.client("bedrock-runtime",region_name="us-east-1",
                             config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
        bedrock.invoke_model(body==json.dumps(body),model="meta.llama2-13b-chat-v1")

        response_content=response.get('body').read()

        


