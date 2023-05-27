import openai
from flask  import Flask,render_template,request
import subprocess




key=openai.api_key="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"
app=Flask("mycmdapp")


@app.route("/home",methods=["GET"])
def chathome():
    prompt=request.args.get("x")
    a=openai.Completion.create(prompt=prompt,model="text-davinci-003",max_tokens=1500)
    ans=(a["choices"][0]['text'])
    data1 =render_template("home.html",mn=ans)
    return data1

app.run(port=5000,debug=True)











