#Functions to save plotly figures optimized for GitHub display
import os
import plotly.io as pio
from IPython.display import Image, display, HTML
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image as PILImage

def save_plot_for_github(fig, filename, width=1200, height=600, 
                         optimize_for_github=True, preview_width=800):
    """Saves a plotly figure optimized for GitHub display.
    
    Args:
        fig: Plotly figure to save
        filename: Base filename (without extension)
        width: Full PNG width in pixels (default: 1200)
        height: Full PNG height in pixels (default: 600)
        optimize_for_github: If True, reduces HTML size (default: True)
        preview_width: Width of preview displayed in notebook (default: 800)
    """
    
    # Creating directories
    os.makedirs('docs', exist_ok=True)
    os.makedirs('docs/images', exist_ok=True)
    
    # Base paths
    png_path = f"docs/images/{filename}.png"           # Full size PNG
    html_path = f"docs/{filename}.html"               # Interactive HTML
    preview_path = f"docs/images/{filename}_preview.png"  # Preview PNG
    
    # 1. Saving FULL-SIZE PNG to files
    try:
        fig.write_image(png_path, width=width, height=height, scale=2)
        print(f"✅ Full PNG saved: {png_path} ({width*2}px wide with scale=2)")
    except Exception as e:
        print(f"⚠️ PNG save failed: {e}")
        png_path = None
    
    # 2. Creating and saving PREVIEW PNG (for notebook display)
    preview_success = False
    if png_path and os.path.exists(png_path):
        try:
            img = PILImage.open(png_path)
            # Creating preview (custom width, default 800px)
            aspect_ratio = height / width
            preview_height = int(preview_width * aspect_ratio)
            img_preview = img.resize((preview_width, preview_height), PILImage.Resampling.LANCZOS)
            img_preview.save(preview_path, optimize=True, quality=90)  # Higher quality
            preview_success = True
            print(f"✅ Preview saved: {preview_path} ({preview_width}px wide)")
        except Exception as e:
            print(f"⚠️ Preview creation failed: {e}")
    
    # 3. Saving OPTIMIZED HTML (CDN version)
    if optimize_for_github:
        try:
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
            
            fig.update_layout(
                template='plotly_white',
                title=dict(x=0.5, font=dict(size=20)),
                showlegend=True
            )
            
            fig.write_html(
                html_path,
                config=optimized_config,
                include_plotlyjs='cdn',
                full_html=False,
                default_height=height,
                default_width=width,
                validate=False 
            )
            file_size_kb = os.path.getsize(html_path)/1024
            print(f"✅ HTML saved: {html_path} ({file_size_kb:.1f} KB)")
            
        except Exception as e:
            print(f"⚠️ HTML save failed: {e}")
            fig.write_html(html_path)
    else:
        fig.write_html(html_path)
        print(f"✅ HTML saved: {html_path}")
    
    # 4. Displaying PREVIEW in notebook (larger size)
    if preview_success and os.path.exists(preview_path):
        # Display the larger preview in notebook
        display(Image(filename=preview_path, width=preview_width))
        print(f"📊 Preview displayed in notebook ({preview_width}px wide)")
    elif png_path and os.path.exists(png_path):
        # Fallback: display full size if preview failed
        display(Image(filename=png_path, width=preview_width))
        print(f"📊 Full PNG displayed in notebook (resized to {preview_width}px)")
    else:
        fig.show()
        print("📊 Plot displayed directly")
    
    # 5. Showing download links for FULL-SIZE files
    display(HTML(f'''
    <div style="background:#f8f9fa; padding:12px; border-radius:8px; border:1px solid #dee2e6; margin-top:12px; color:black;">
    <strong>📁 Download Full-Size Files:</strong><br>
    • <a href="{png_path or '#'}" download>📸 Full PNG</a> ({width*2}px wide - high resolution)<br>
    • <a href="{html_path or '#'}" download>🖥️ Interactive HTML</a> (zoom, hover, explore)<br>
    <small><em>Displayed above: {preview_width}px preview for notebook viewing</em></small>
    </div>
    '''))
    
    return {
        'png_full': png_path,      # Full size PNG
        'preview': preview_path,   # Preview PNG
        'html': html_path,         # Interactive HTML
        'preview_width': preview_width
    }