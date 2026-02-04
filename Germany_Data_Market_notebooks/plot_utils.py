# Optimizing Plotly Visualizations for GitHub: A Comprehensive Guide
import os
import plotly.io as pio
from IPython.display import Image, display, HTML
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image as PILImage
import io

# Defining a function to save Plotly figures optimized for GitHub display
def save_plot_for_github(fig, filename, width=1200, height=600, 
                         optimize_for_github=True):
    """Saves a plotly figure optimized for GitHub display.
    
    GitHub-friendly approach: Prioritizes PNG, creates optimized HTML,
    and provides proper download links.
    
    Args:
        fig (plotly.graph_objects.Figure): Plotly figure to save
        filename (str): Base filename (without extension)
        width (int): Image width in pixels
        height (int): Image height in pixels
        optimize_for_github (bool): If True, reduces HTML size drastically
    """
    
    # Creating directories
    os.makedirs('docs', exist_ok=True)
    os.makedirs('docs/images', exist_ok=True)
    
    # Base paths
    png_path = f"docs/images/{filename}.png"
    html_path = f"docs/{filename}.html"
    readme_path = f"docs/images/{filename}_preview.png"  # Smaller version for README
    
    # Saving high-quality PNG using kaleido (much smaller than HTML)
    try:
        # Save the full-size PNG
        fig.write_image(png_path, width=width, height=height, scale=2)
        print(f"✅ Saved PNG: {png_path}")
        
        # Creating smaller preview for README (600px wide)
        if os.path.exists(png_path):
            img = PILImage.open(png_path)
            # Calculating proportional height for 600px width
            aspect_ratio = height / width
            new_width = 600
            new_height = int(new_width * aspect_ratio)
            img_resized = img.resize((new_width, new_height), PILImage.Resampling.LANCZOS)
            img_resized.save(readme_path, optimize=True, quality=85)
            print(f"✅ Created README preview: {readme_path}")
        
    except Exception as e:
        print(f"⚠️ Could not save PNG (install: pip install kaleido): {e}")
        png_path = None
    
    # Saving optimized HTML (much smaller than default)
    if optimize_for_github:
        # Reducing HTML file size by removing unnecessary elements
        try:
            # Create optimized config
            optimized_config = {
                'displaylogo': False,
                'modeBarButtonsToRemove': [
                    'lasso2d', 'select2d', 'autoScale2d',
                    'toggleSpikelines', 'hoverCompareCartesian',
                    'hoverClosestCartesian'
                ],
                'displayModeBar': True,
                'responsive': True
            }
            
            # Updating layout for smaller HTML
            fig.update_layout(
                template='plotly_white',
                title=dict(x=0.5, font=dict(size=20)),
                showlegend=True
            )
            
            # Saving with compression
            fig.write_html(
                html_path,
                config=optimized_config,
                include_plotlyjs='cdn',  # Using CDN instead of embedding 
                full_html=False,  
                default_height=height,
                default_width=width,
                validate=False 
            )
            print(f"✅ Saved optimized HTML: {html_path} ({os.path.getsize(html_path)/1024:.1f} KB)")
            
        except Exception as e:
            print(f"⚠️ Error saving optimized HTML: {e}")
            # Fallback to regular HTML
            fig.write_html(html_path)
    else:
        # Regular HTML save
        fig.write_html(html_path)
        print(f"✅ Saved HTML: {html_path}")
    
    # Displaying the PNG preview in the notebook
    if png_path and os.path.exists(png_path):
        # Display smaller preview in notebook
        display(Image(filename=png_path, width=800))
    else:
        # Showing the figure directly if PNG failed
        fig.show()
    
    # Generating markdown for README.md
    markdown_text = f"""
## 📊 {filename.replace('_', ' ').title()}

![{filename}](docs/images/{filename}_preview.png)
*Click image to view full size*

[📥 Download full resolution PNG](docs/images/{filename}.png) | 
[🔗 View interactive HTML](docs/{filename}.html)
    """
    
    print("\n" + "="*60)
    print("📋 **MARKDOWN FOR README.md:**")
    print("="*60)
    print(markdown_text)
    print("="*60)
    
    # Adding interactive download links in the notebook
    display(HTML(f'''
    <div style="background:#f8f9fa; padding:15px; border-radius:8px; border:1px solid #dee2e6; margin-top:20px;">
    <strong>📁 Files Saved:</strong><br>
    • <a href="{png_path}" download>📸 {os.path.basename(png_path)}</a> (Static image)<br>
    • <a href="{html_path}" download>🖥️ {os.path.basename(html_path)}</a> (Interactive)<br>
    • <a href="{readme_path}" download>📱 {os.path.basename(readme_path)}</a> (README preview)<br><br>
    <small><em>Copy the markdown above to your README.md</em></small>
    </div>
    '''))
    
    return {
        'png': png_path,
        'html': html_path,
        'preview': readme_path,
        'markdown': markdown_text
    }

def create_simple_bar_chart(df, x_col, y_col, title, xaxis_title=None, yaxis_title=None):
    """Creates a simple bar chart optimized for GitHub."""
    
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        title=title,
        color=y_col,
        color_continuous_scale='Blues',
        text_auto='.0f'
    )
    
    fig.update_layout(
        title=dict(x=0.5, font=dict(size=24)),
        xaxis_title=xaxis_title or x_col,
        yaxis_title=yaxis_title or y_col,
        plot_bgcolor='white',
        showlegend=False,
        height=500,
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    fig.update_traces(
        textfont_size=14,
        textposition='outside',
        marker_line_color='darkblue',
        marker_line_width=0.5
    )
    
    return fig

# Install helper function
def install_requirements():
    """Prints installation instructions for required packages."""
    
    instructions = """
    =============================================================================
    📦 REQUIRED PACKAGES FOR OPTIMIZED PLOTS:
    =============================================================================
    
    1. Install kaleido for static PNG export:
       pip install kaleido
       
    2. Optional optimizations:
       pip install pillow  # For image resizing
       
    3. If using Plotly in Jupyter:
       pip install ipywidgets
       jupyter nbextension enable --py widgetsnbextension
       
    =============================================================================
    """
    print(instructions)
    
    return instructions
