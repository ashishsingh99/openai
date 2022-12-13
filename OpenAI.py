import openai
# from dotenv import dotenv_values

# config = dotenv_values('.env')

openai.api_key = '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'

def generate_blog(paragraph_topic):
  response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 2000,
    temperature = 1
  )
  retrieve_blog = response.choices[0].text
  return retrieve_blog

# Multiple Paragraphs

keep_writing = True
answer = input('Write a paragraph? Y for yes, anything else for no. ')
paragraph_topic = input('What should this paragraph talk about? ')
while keep_writing:
  # answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    # paragraph_topic = input('What should this paragraph talk about? ')
    for i in range(5):
      print(generate_blog(paragraph_topic))
      i=i+1
  break
else:
  keep_writing = False