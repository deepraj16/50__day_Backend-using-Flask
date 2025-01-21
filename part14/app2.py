from flask import Flask,render_template
import matplotlib.pyplot as plt
import os
import numpy as np 
import base64 
import io
from wordcloud import WordCloud
import plotly.graph_objects as px

app=Flask(__name__)

@app.route("/")
def admin():
    return render_template("index1.html")

@app.route("/first-plot")
def home():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    
    # Generate sample dataclz
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    x1 = np.linspace(-5, 5, 100)
    y1 = np.sin(x1)
    # Create a surface plot
    ax.plot(x1,y1)
    ax.set_title("3D Surface Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    #ax.set_zlabel("Z-axis")
    
    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return render_template('index2.html', graph_url=graph_url)

@app.route("/wordcloud")
def plot():
    h="flask is very good for backend but flask is light weight"
    wordcloud=WordCloud(width= 800, height = 400,background_color='white').generate(h)
    img=io.BytesIO()
    plt.figure(figsize=(8,4))
    plt.imshow(wordcloud, interpolation='bilinear')   
    plt.axis('off')
    plt.tight_layout()    
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    wordcloud_url = base64.b64encode(img.getvalue()).decode()
    plt.close() 

    return render_template("index3.html",word=wordcloud_url)
    
@app.route("/plot3d")
def plot3D():
    x=np.linspace(-5,5,50)
    y=np.linspace(-5,5,50)
    X,Y =np.meshgrid(x,y)
    Z=np.sin(np.sqrt(X**2+Y**2))

    fig=px.Figure(data=[px.Surface(z=Z,x=X[0],y=Y[:,0], colorscale='Viridis')])
    fig.update_layout(
        title="3D Suraface plot (plotly)",
        scence=dict(
           xaxis_title="X-axis",
            yaxis_title="Y-axis",
            zaxis_title="Z-axis"
        )
    )

    plot_html =fig.to_html(full_html=False)
    return render_template("index4.html",plot_html=plot_html)


if __name__ == "__main__":
    app.run(debug=True)
