from flask import Flask, render_template
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from wordcloud import WordCloud
import numpy as np
import io
import base64
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plot3d')
def plot3d():
    # Create a 3D Matplotlib figure
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate sample data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Create a surface plot
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title("3D Surface Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    
    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return render_template('plot3d.html', graph_url=graph_url)

@app.route('/wordcloud')
def wordcloud():
    # Generate Word Cloud data
    text = "Flask Python Matplotlib 3D Plot Word Cloud Data Science Machine Learning"
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Save the word cloud to a BytesIO object
    img = io.BytesIO()
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    wordcloud_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return render_template('wordcloud.html', wordcloud_url=wordcloud_url)


@app.route('/plot3d-plotly')
def plot3d_plotly():
    # Generate Plotly 3D plot data
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    # Create Plotly figure
    fig = go.Figure(data=[go.Surface(z=Z, x=X[0], y=Y[:, 0], colorscale='Viridis')])
    fig.update_layout(
        title="3D Surface Plot (Plotly)",
        scene=dict(
            xaxis_title="X-axis",
            yaxis_title="Y-axis",
            zaxis_title="Z-axis"
        )
    )
    
    # Convert the plot to an HTML div string
    plot_html = fig.to_html(full_html=False)
    return render_template('plot3d_plotly.html', plot_html=plot_html)


if __name__ == '__main__':
    app.run(debug=True)
