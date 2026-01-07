from transformers import pipeline

def main ():
    generator = pipeline(
        task = "text-generation",
        model = "gpt2",
        max_new_tokens = 100,               # length of output
        temperature = 0.7                 # for creativity
    )

    input_topic = input("enter topic: ")
    output = generator(input_topic)                       # output is a list
    print(output[0]["generated_text"])

if __name__ == "__main__":
    main()    



'''
Other tasks for which I can use HF pipelines for.. are listed below..
text2text-generation
fill-mask                       (ex: "I love to <mask> apples")
sentiment-analysis
question-answering
summarization
translation           (text to different language)
'''    