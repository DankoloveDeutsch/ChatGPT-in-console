import openai

class DaVinchi:
    def __init__(self, OPEN_AI_TOKEN):
        openai.api_key = OPEN_AI_TOKEN
        self.model_name = 'text-davinci-003'

    def send_question(self, question: str) -> str:
        params = {
            "max_tokens": 2048,
            "temperature": 0.3,
            "top_p": 0.7,
            "frequency_penalty": 0.2,
            "presence_penalty": 0.1
        }
        response = openai.Completion.create(
            model=self.model_name,
            prompt=f"{question}",
            **params
        )
        if len(response['choices']) == 0:
            return "Not result"
        result = response['choices'][0]['text']
        return result

def main():
	dv = DaVinchi("Your api_key_openai")
	while(1):
		question = input('input question: ')
		result = dv.send_question(question)
		print(result)

if __name__ == '__main__':
	main()
