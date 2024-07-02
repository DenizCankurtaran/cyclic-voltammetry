import streamlit as st
import streamlit.components.v1 as components

#if you have specified a theme, you can get the border color with:
#border = st.get_option('theme.secondaryBackgroundColor')
#border = 'rgb(49,51,63,.2)' #light mode
border = 'rgb(250,250,250,.2)' #dark mode

def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}';
                    elements[i].onfocus = function() {{
                        this.style.boxShadow = '{font_color} 0px 0px 0px 0.2rem';
                        this.style.borderColor = '{font_color}';
                        this.style.color = '{font_color}';
                    }};
                    elements[i].onblur = function() {{
                        this.style.boxShadow = 'none';
                        this.style.borderColor = '{border}';
                        this.style.color = '{font_color}';
                    }};
                }}
            }}
            }});
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)
