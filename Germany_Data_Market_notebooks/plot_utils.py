# Creating re-usable file for data market analysis in Germany
import os
import plotly.io as pio
from IPython.display import Image, display, HTML
import plotly.graph_objects as go

# Function to display images in Jupyter Notebooks
def save_plot_for_github(fig, filename, width=800, height=600):
    """Saves a plotly figure as a PNG image for GitHub display.

    Args:
        fig (plotly.graph_objects.Figure): The plotly figure to save.
        filename (str): The name of the file to save the image as.
        width (int, optional): Width of the image. Defaults to 800.
        height (int, optional): Height of the image. Defaults to 600.
    """
    # Creating images directory
    os.makedirs('docs/images', exist_ok=True)

    # Saving interactive HTML (for local use)
    html_path = f"docs/images/{filename}.html"
    fig.write_html(html_path)

    # Trying to save static PNG (for GitHub) 
    png_path =f"docs/images/{filename}.png"
    try:
        fig.write_image(png_path, width=width, height=height)
        print(f"Saved: {png_path} (static) and {html_path} (interactive)")

        # Displaying static image in Jupyter Notebook
        display(Image(filename=png_path))

        # Adding download link for interactive HTML
        display(HTML(f'📥 <a href="{html_path}" target="_blank">Download interactive version</a>'))

    except Exception as e:
        print(f"⚠️ Could not save PNG (kaleido missing): {e}")
        print(f"✅ Still saved interactive HTML: {html_path}")

        # Showing message for Github viewers
        display(HTML(f'''
        <div style="background:#f0f8ff; padding:15px; border-left:4px solid #4CAF50;">
        <strong>📊 Interactive Plot</strong><br>
        This plot requires the kaleido package to display as static image.<br>
        <a href="{html_path}" target="_blank">Download HTML version</a> to view interactively.
        </div>
        '''))

    return png_path, html_path