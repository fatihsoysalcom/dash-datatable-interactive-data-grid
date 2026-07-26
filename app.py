import dash
from dash import dcc, html, dash_table
import pandas as pd

# Sample data for the data grid
# This DataFrame represents typical data that would be displayed in an interactive table.
data = {
    'Ürün Adı': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Headphones', 'SSD', 'RAM'],
    'Kategori': ['Elektronik', 'Aksesuar', 'Aksesuar', 'Elektronik', 'Aksesuar', 'Aksesuar', 'Depolama', 'Depolama'],
    'Fiyat (TL)': [12000, 250, 750, 4500, 300, 600, 1500, 800],
    'Stok Miktarı': [50, 200, 100, 30, 150, 80, 70, 120]
}
df = pd.DataFrame(data)

# Initialize the Dash application
app = dash.Dash(__name__)

# Define the application layout
app.layout = html.Div([
    html.H1("Ürün Stok Durumu (Dash Veri Izgarası)"),
    html.P("Bu örnek, Dash'in etkileşimli veri izgarası bileşenini (DataTable) göstermektedir."),

    # The core Dash DataTable component, demonstrating an interactive data grid
    dash_table.DataTable(
        id='table-interactive-products',
        columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
        data=df.to_dict('records'),

        # Enable client-side filtering: users can type into a filter row below headers
        filter_action="native", 

        # Enable client-side sorting: users can click column headers to sort
        sort_action="native",   

        # Enable client-side pagination: adds controls to navigate through pages
        page_action="native",   
        page_size=5,            # Display 5 rows per page

        # Enable cell editing: users can directly modify cell values
        editable=True,          

        # Basic styling for better presentation
        style_table={'overflowX': 'auto'},
        style_cell={
            'height': 'auto',
            'minWidth': '80px', 'width': '150px', 'maxWidth': '250px',
            'whiteSpace': 'normal'
        },
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )
])

# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)
