import openai
import csv
import time

openai.api_key = "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"
#create configuration 

def get_model_reply(query, context=[]):
  # combines the new question with a previous context
  context += [query]

  # given the most recent context (4096 characters)
  # continue the text up to 2048 tokens ~ 8192 charaters
  completion = openai.Completion.create(
    engine='text-davinci-003',  # one of the most capable models available
    prompt='\n\n'.join(context)[:4096],
    max_tokens=2048,
    temperature=0.5,  # Lower values make the response more deterministic
  )

  # append response to context
  response = completion.choices[0].text.strip('\n')
  context += [response]

  # list of (user, bot) responses. We will use this format later
  responses = [(u, b) for u, b in zip(context[::2], context[1::2])]

  return responses, context


with open(r'fakeprofile1000.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    first_name, last_name, birth_year, pet_name, phone_number, random_pattern = row
    print(row)
    time.sleep(10)
    query = f"""i am going to send to u features for fake profiles and i need u to think as average internet user and generate 10 passwords for different platforms that user might create based on features First Name: {first_name} Last Name: {last_name} Birth Year: {birth_year} Pet Name: {pet_name} Phone   Number: {phone_number} Random Pattern: {random_pattern}"""
  print('USER: ' + responses[-1][0])

  responses, context = get_model_reply(query, context=[])
  with open('response.csv','a', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow([responses[-1][0], responses[-1][1]])  

  print('BOT: ' + responses[-1][1])