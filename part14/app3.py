from flask import Flask 
import matplotlib.pyplot as plt 
from plotly.express import scatter_3d 
import numpy as np 
import base64 
import io
import os 
from wordcloud import WordCloud 


app =Flask(__name__) 



@app.route("/")
def home():
    X=np.linspace(10,40,30)
    y=np.sin(y)
    img=io.B
    h="Flask is best the the other django"
    word=WordCloud(width=500,height=800,background_color="white").generate(h)
    plt.figure(figsize=(8,4))
    plt.imshow(word,interpolation='bilinear')
    plt.tight_layout() 
    plt.savefig(img,format='png',bbox_inches='tight')
    img.seek(0)
    wordcloud_url=base64.b64encode(img.getvalue())
    return "hellow"

if __name__ =="__main__":
    app.run(debug=True)