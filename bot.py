# app.py
from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    category = request.json.get('category')
    # Load your dataset
    file_path = "C:/vibebotproject/Amazon_data.xlsx"
    df = pd.read_excel("C:/vibebotproject/Amazon_data.xlsx")
    
    # Filter products by category and positive sentiment
    filtered_products = df[(df['category'].str.lower() == category.lower()) & (df['sentiment'] == 'Positive')]

    if filtered_products.empty:
        return jsonify({"message": "No highly rated products found."}), 404

    # Sort and select the top products
    top_products = filtered_products.sort_values(by='rating', ascending=False).head(5)

    recommendations = []
    for _, row in top_products.iterrows():
        recommendations.append({
            "product_name": row['product_name'],
            "price": f"₹{row['discounted_price']}",
            "rating": row['rating'],
            "product_link": row['product_link'],
        })

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
